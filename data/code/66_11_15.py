def find_violating_pairs(arr):
    violating_indices = []
    n = len(arr)
    for i in range(n - 1):
        if arr[i+1] < arr[i]:
            violating_indices.append((i, i + 1))
    return violating_indices

if __name__ == '__main__':
    sample_array = [1.0, 2.5, 3.1, 2.8, 4.0, 5.5]
    result = find_violating_pairs(sample_array)
    for start, end in result:
        print(f"Indices: ({start}, {end})")