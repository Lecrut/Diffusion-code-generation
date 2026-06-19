def find_adjacent_greater_indices(arr):
    indices = []
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    SAMPLE_ARRAY = [3, 5, 2, 8, 6, 7, 4]
    RESULT = find_adjacent_greater_indices(SAMPLE_ARRAY)
    print(RESULT)