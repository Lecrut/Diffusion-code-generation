import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
def generate_and_visualize_report():
    dates = [datetime.now() + pd.Timedelta(days=i) for i in range(30)]
    values = [round(i * 1.5, 2) for i in range(30)]
    df = pd.DataFrame({
        'date': dates,
        'value': values
    })
    fig, ax = plt.subplots(figsize=(10, 6))
    line_plot = ax.plot(df['date'], df['value'], marker='o', linestyle='-')
    ax.grid(True, alpha=0.3)
    ax.set_xlabel('Date', fontsize=12)
    ax.set_ylabel('Value', fontsize=12)
    ax.set_title(f'Daily Value Trend Report - Generated on {datetime.now().strftime("%Y-%m-%d %H:%M")}', 
                 fontweight='bold')
    for i, (date, val) in enumerate(zip(df['date'], df['value'])):
        ax.annotate(f'{val:.2f}', xy=(date, val), textcoords="offset points", 
                   bbox=dict(boxstyle='round,pad=0.5', fc='white'), fontsize=9)
    plt.tight_layout()
    return fig, df
if __name__ == '__main__':
    report_fig, data_df = generate_and_visualize_report()
    print("Report generated successfully.")