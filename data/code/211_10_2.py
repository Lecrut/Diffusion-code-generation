import numpy as np

def compare_data(sample1, sample2):
    mean1 = np.mean(sample1)
    median1 = np.median(sample1)
    std_dev1 = np.std(sample1)

    mean2 = np.mean(sample2)
    median2 = np.median(sample2)
    std_dev2 = np.std(sample2)

    return {
        'sample1': {'mean': mean1, 'median': median1, 'std_dev': std_dev1},
        'sample2': {'mean': mean2, 'median': median2, 'std_dev': std_dev2}
    }

if __name__ == '__main__':
    sample1 = [10, 20, 30, 40, 50]
    sample2 = [15, 25, 35, 45, 55]

    result = compare_data(sample1, sample2)
    print(result)