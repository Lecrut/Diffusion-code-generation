def find_adjacent_greater_pairs(arr):
    indices = []
    n = len(arr)
    for i in range(n - 1):
        if arr[i+1] > arr[i]:
            indices.append((i, i+1))
    return indices
if __name__ == '__main__':
    sample_array = [1, 3, 2, 5, 4, 6, 7]
    result = find_adjacent_greater_pairs(sample_array)
    for start, end in result:
        print(f"Indices: ({start}, {end})")