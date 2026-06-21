import numpy as np

def calculate_statistics(data_set):
    return {
        'mean': np.mean(data_set),
        'median': np.median(data_set),
        'std_dev': np.std(data_set)
    }

if __name__ == '__main__':
    sample_data_set_1 = [10, 20, 30, 40, 50]
    sample_data_set_2 = [15, 25, 35, 45, 55]

    stats_1 = calculate_statistics(sample_data_set_1)
    stats_2 = calculate_statistics(sample_data_set_2)

    print(f"Statistics for Sample Data Set 1: {stats_1}")
    print(f"Statistics for Sample Data Set 2: {stats_2}")