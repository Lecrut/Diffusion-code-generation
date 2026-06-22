def average_small_arrays(arrays):
    return [sum(arr) / len(arr) for arr in arrays]

if __name__ == '__main__':
    sample_arrays = [[1, 2, 3], [4, 5], [6, 7, 8, 9]]
    print(average_small_arrays(sample_arrays))