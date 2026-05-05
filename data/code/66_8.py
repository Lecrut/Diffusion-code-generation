def find_descending_pairs(arr):
    indices = []
    n = len(arr)
    if n < 2:
        return indices
    for i in range(n - 1):
        if arr[i] > arr[i+1]:
            indices.append(i)
    return indices
if __name__ == '__main__':
    sample_array = [1, 5, 4, 2, 8, 3, 7]
    result = find_descending_pairs(sample_array)
    print(result)