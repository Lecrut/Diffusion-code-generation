def validate_input(data):
    if not isinstance(data, list) or len(data) < 2:
        raise ValueError("Input must be a list with at least two elements.")

def compare_adjacent_elements(arr):
    validate_input(arr)
    return [arr[i] > arr[i - 1] for i in range(1, len(arr))]

if __name__ == '__main__':
    sample_array = [1.0, 2.5, 3.0, 3.0, 5.1, 6.0, 6.0, 7.5]
    result = compare_adjacent_elements(sample_array)
    print(result)