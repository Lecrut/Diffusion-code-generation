def find_adjacent_greater_indices(arr):
    indices = []
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    sample_array = [3, 5, 2, 4, 8, 7, 6]
    result = find_adjacent_greater_indices(sample_array)
    print(result)