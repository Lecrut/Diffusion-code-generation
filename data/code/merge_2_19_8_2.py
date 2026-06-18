import pandas as pd
import matplotlib.pyplot as plt
def generate_and_visualize():
    data = {
        'id': range(10),
        'value_a': [float(i * 2.5) for i in range(10)],
        'value_b': [i ** 2 / 3 + 4 for i in range(10)]
    }
    df = pd.DataFrame(data)
    plt.style.use('seaborn-v0_8-whitegrid')
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(df['id'], df['value_a'], marker='o', color='#FF5733', linewidth=2.5)
    ax.set_xlabel('ID', fontsize=14, fontweight='bold')
    ax.set_ylabel('Value A', fontsize=14, fontweight='bold')
    ax.scatter(df['id'], df['value_b'], color='#33FF57', s=80, alpha=0.6)
    ax.legend(['Series A (Line)', 'Series B (Scatter)'])
    ax.set_title('Automated Dataset Visualization Report', fontsize=16, fontweight='bold')
    plt.grid(True, linestyle='--', alpha=0.7)
    return df
if __name__ == '__main__':
    report_df = generate_and_visualize()
    print("Report generated successfully.")