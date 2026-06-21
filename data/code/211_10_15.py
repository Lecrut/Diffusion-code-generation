import numpy as np

def compare_data_sets(data_set_1, data_set_2):
    mean_1 = np.mean(data_set_1)
    median_1 = np.median(data_set_1)
    std_dev_1 = np.std(data_set_1)

    mean_2 = np.mean(data_set_2)
    median_2 = np.median(data_set_2)
    std_dev_2 = np.std(data_set_2)

    return {
        'mean_1': mean_1,
        'median_1': median_1,
        'std_dev_1': std_dev_1,
        'mean_2': mean_2,
        'median_2': median_2,
        'std_dev_2': std_dev_2
    }

if __name__ == '__main__':
    sample_data_set_1 = [1, 2, 3, 4, 5]
    sample_data_set_2 = [5, 4, 3, 2, 1]

    results = compare_data_sets(sample_data_set_1, sample_data_set_2)
    print(results)