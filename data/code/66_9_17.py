def find_adjacent_greater_pairs(arr):
    indices = []
    for i in range(len(arr) - 1):
        if arr[i + 1] > arr[i]:
            indices.append(i)
    return indices

if __name__ == '__main__':
    sample_array = [10, 20, 30, 25, 40, 50]
    result = find_adjacent_greater_pairs(sample_array)
    print(result)