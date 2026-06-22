import numpy as np

def calculate_small_set_average(list_of_lists):
    arr = np.array(list_of_lists)
    non_zero_sums = np.where(arr != 0, arr.sum(axis=1), 0)
    non_zero_counts = np.where(arr != 0, 1, 0).sum(axis=1)
    averages = np.where(non_zero_counts == 0, 0, non_zero_sums / non_zero_counts)
    return averages.tolist()
if __name__ == '__main__':
    sample_data = [[1, 2, 3], [10, 20, 30], [5, 5, 5], [], [7, 8]]
    result = calculate_small_set_average(sample_data)
    print(result)