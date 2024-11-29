def xtline(df, unit_col, time_col, value_col, title=None, xlabel=None, ylabel=None):
    import matplotlib.pyplot as plt
    import math
    import seaborn as sns
    import warnings
    warnings.filterwarnings("ignore")
    units = df[unit_col].unique()
    n_units = len(units)
    colors = sns.color_palette("husl", n_units)
    cols = 3
    rows = math.ceil(n_units / cols)
    
    # Criando a figura
    fig, axes = plt.subplots(rows, cols, figsize=(15, 5 * rows))
    axes = axes.flatten()  # Facilita o acesso aos eixos
    
    # Iterando pelas unidades e gerando os gráficos
    for i, (unit, color) in enumerate(zip(units, colors)):
        unit_data = df[df[unit_col] == unit]
        axes[i].plot(unit_data[time_col], unit_data[value_col], color=color, label=f'Unit {unit}')
        axes[i].set_title(f'{unit}')
        axes[i].set_xlabel(xlabel if xlabel else 'Time')
        axes[i].set_ylabel(ylabel if ylabel else 'Value')
        axes[i].grid(True)
        axes[i].legend()
    
    # Removendo eixos vazios, se necessário
    for j in range(i + 1, len(axes)):
        fig.delaxes(axes[j])
    
    # Adicionando o título geral
    if title:
        fig.suptitle(title, fontsize=16, fontweight='bold', y=1.02)  # Ajusta a posição do título
    
    # Ajustando o layout
    plt.tight_layout()
    plt.show()
