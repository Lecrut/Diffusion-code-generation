import numpy as np

def compare_data(data1, data2):
    mean1 = np.mean(data1)
    median1 = np.median(data1)
    std1 = np.std(data1)

    mean2 = np.mean(data2)
    median2 = np.median(data2)
    std2 = np.std(data2)

    print(f"Data 1 Mean: {mean1}, Median: {median1}, Standard Deviation: {std1}")
    print(f"Data 2 Mean: {mean2}, Median: {median2}, Standard Deviation: {std2}")

if __name__ == '__main__':
    sample_data1 = [1, 2, 3, 4, 5]
    sample_data2 = [5, 4, 3, 2, 1]

    compare_data(sample_data1, sample_data2)