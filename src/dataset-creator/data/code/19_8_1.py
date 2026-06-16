import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta
def generate_sample_data():
    return {
        'Date': [datetime.now() - timedelta(days=i) for i in range(30)],
        'Revenue': [12.5 + 2 * (i ** 0.8) if i < 20 else 40 + 0.5 * i for i in range(30)],
        'Users': [100 + 15 * i - 2 * i**2 / 10 for i in range(30)]
    }
def create_visualization(data):
    fig, ax = plt.subplots(figsize=(10, 6))
    df = pd.DataFrame(data)
    ax.plot(df['Date'], df['Revenue'], marker='o', label='Revenue')
    ax.set_xlabel('Time (Days)', fontsize=12)
    ax.set_ylabel('Amount ($)', fontsize=12)
    ax.legend(loc='upper right')
    ax.grid(True, linestyle='--', alpha=0.7)
    plt.xticks(rotation=45)
    plt.tight_layout()
def generate_report():
    data = generate_sample_data()
    df = pd.DataFrame(data)
    print(f"Generated dataset with {len(df)} records.")
    create_visualization(data)
    return df, fig if 'fig' in locals() else None
if __name__ == '__main__':
    try:
        report_df, _ = generate_report()
    except Exception as e:
        print(f"Error generating report: {e}")