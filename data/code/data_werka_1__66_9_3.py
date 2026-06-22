def find_adjacent_greater_pairs(arr):
    indices = []
    for index in range(len(arr) - 1):
        if arr[index + 1] > arr[index]:
            indices.append(index)
    return indices

if __name__ == '__main__':
    test_array = [7, 1, 5, 3, 9, 2, 8]
    greater_indices = find_adjacent_greater_pairs(test_array)
    print(greater_indices)