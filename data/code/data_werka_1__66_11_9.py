def validate_input(arr):
    if not isinstance(arr, list) or not all(isinstance(x, float) for x in arr):
        raise ValueError("Input must be a list of floats.")

def find_adjacent_greater_pairs(arr):
    validate_input(arr)
    indices = []
    n = len(arr)
    for i in range(n - 1):
        if arr[i + 1] > arr[i]:
            indices.append((i, i + 1))
    return indices

if __name__ == '__main__':
    sample_array = [1.0, 3.5, 2.0, 5.5, 4.0, 7.0, 6.0]
    result = find_adjacent_greater_pairs(sample_array)
    for start, end in result:
        print(f"Indices: ({start}, {end})")