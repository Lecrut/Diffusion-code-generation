import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
def generate_report():
    data = {
        'date': pd.date_range(start='2023-01-01', periods=5, freq='D'),
        'sales': [120.5, 145.8, 167.2, 190.1, 210.3],
        'expenses': [80.2, 95.4, 110.6, 125.8, 140.1]
    }
    df = pd.DataFrame(data)
    plt.figure(figsize=(10, 6))
    ax = plt.subplot()
    ax.plot(df['date'], df['sales'], marker='o', label='Sales Revenue')
    ax.plot(df['date'], df['expenses'], marker='s', label='Operating Expenses')
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.legend(frameon=True, loc='upper left')
    plt.title('Monthly Financial Performance Report (January 2023)', fontsize=14)
    ax.xaxis.set_major_formatter(plt.matplotlib.dates.DateFormatter('%b %Y'))
    fig = plt.gcf()
    fig.autofmt_xdate()
    return df, fig
if __name__ == '__main__':
    data_frame, figure_obj = generate_report()
    save_path = f'financial_report_{datetime.now().strftime("%Y%m%d_%H%M%S")}.png'
    plt.savefig(save_path)
    print(f"Report generated successfully: {save_path}")