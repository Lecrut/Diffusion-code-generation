def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        if not isinstance(item, (int, float)):
            raise ValueError(f"Invalid element type: {type(item).__name__}. All elements must be numbers.")
def filter_positive_numbers(data):
    validate_input(data)
    return [num for num in data if num > 0]
if __name__ == '__main__':
    sample_data = [-5, 10, -3.5, 20, 'invalid', 7.8]
    try:
        result = filter_positive_numbers(sample_data)
        print(f"Filtered positive numbers: {result}")
    except (TypeError, ValueError) as e:
        print(f"Error: {e}")