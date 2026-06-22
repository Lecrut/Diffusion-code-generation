def average_small_arrays(arrays):
    return [sum(array) / len(array) for array in arrays]

if __name__ == '__main__':
    sample_arrays = [[1, 2, 3], [4, 5], [6]]
    print(average_small_arrays(sample_arrays))