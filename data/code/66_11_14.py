def validate_input(arr):
    if not isinstance(arr, list):
        raise ValueError("Input must be a list.")
    for x in arr:
        if not isinstance(x, float):
            raise ValueError("All elements in the list must be floats.")

def find_adjacent_greater_pairs(arr):
    validate_input(arr)
    indices = []
    n = len(arr)
    for i in range(n - 1):
        if arr[i+1] > arr[i]:
            indices.append((i, i+1))
    return indices

if __name__ == '__main__':
    sample_array = [1.0, 3.0, 2.0, 5.0, 4.0, 6.0, 7.0]
    result = find_adjacent_greater_pairs(sample_array)
    for start, end in result:
        print(f"Indices: ({start}, {end})")