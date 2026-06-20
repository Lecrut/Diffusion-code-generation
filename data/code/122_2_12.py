import numpy as np

def average_with_handling(arr):
    count = np.count_nonzero(~np.isnan(arr))
    if count == 0:
        return np.nan
    return np.sum(arr) / count

if __name__ == '__main__':
    sample_array = np.array([1.5, 2.3, np.nan, 4.1])
    result = average_with_handling(sample_array)
    print(result)