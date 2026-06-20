import numpy as np

def average_with_handling(arr):
    sum_arr = np.sum(arr)
    count = arr.size
    if count == 0:
        return np.nan
    avg = sum_arr / count
    return avg

if __name__ == '__main__':
    sample_array = np.array([1.5, 2.5, 3.5, 4.5])
    print(average_with_handling(sample_array))