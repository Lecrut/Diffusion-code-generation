def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        if not isinstance(item, (int, float)) and not isinstance(item, complex):
            return False
    return True
def filter_positive_numbers(input_data):
    if not validate_input(input_data):
        raise ValueError("Invalid input provided.")
    filtered = [num for num in input_data if num > 0]
    return filtered
if __name__ == '__main__':
    sample_list = [-5, 10, -3.5, 20, 'invalid', 42, None]
    try:
        result = filter_positive_numbers(sample_list)
        print(f"Filtered positive numbers: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")