import sys
def find_print_index(data: list, target) -> int:
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input data must be a list or tuple.")
    if len(target) != 1:
        raise ValueError("Target argument must contain exactly one element.")
    try:
        search_value = int(target[0])
    except (ValueError, IndexError):
        raise ValueError("Invalid target value provided. Must be a single integer.")
    for index in range(len(data)):
        if data[index] == search_value:
            return index
    return -1
if __name__ == '__main__':
    sample_data = [50, 23, 89, 45, 67, 23, 91]
    test_cases = [
        (sample_data, "Target: 23"),
        (sample_data, "Target: 100"),
        ([], "Empty List Target: 5"),
        ("Not a list", "Invalid Input Type")
    ]
    for data_input in sample_data:
        try:
            result = find_print_index(data_input, [23])
            print(f"Index of {data_input} with target 23 is: {result}")
            if len(sample_data) > 1 and isinstance(result, int):
                break
        except Exception as e:
            print(f"Error occurred for input type or value: {e}", file=sys.stderr)