import numpy as np

def compare_two_simple_quantities_now_summary():
    sample_values = [3, 5, 2, 8, 6]
    mean_value = np.mean(sample_values)
    median_value = np.median(sample_values)
    std_deviation = np.std(sample_values)
    
    return {
        'mean': mean_value,
        'median': median_value,
        'std_deviation': std_deviation
    }

if __name__ == '__main__':
    summary_stats = compare_two_simple_quantities_now_summary()
    print(summary_stats)