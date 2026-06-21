import numpy as np

def compare_data(data1, data2):
    mean1 = np.mean(data1)
    median1 = np.median(data1)
    std_dev1 = np.std(data1)

    mean2 = np.mean(data2)
    median2 = np.median(data2)
    std_dev2 = np.std(data2)

    return {
        'mean_diff': mean1 - mean2,
        'median_diff': median1 - median2,
        'std_dev_ratio': std_dev1 / std_dev2
    }

if __name__ == '__main__':
    sample_data1 = [1, 2, 3, 4, 5]
    sample_data2 = [5, 4, 3, 2, 1]

    result = compare_data(sample_data1, sample_data2)
    print(result)