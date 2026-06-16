import sys
def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        if not isinstance(item, (int, float)) and not isinstance(item, complex):
            return False
    return True
def filter_positive_numbers(input_data):
    result = []
    for num in input_data:
        if num >= 0:
            result.append(num)
    return result
if __name__ == '__main__':
    sample_values = [-5, -1.2, 3, 0, 7.89]
    try:
        is_valid = validate_input(sample_values)
        if not is_valid:
            print("Input validation failed.")
            sys.exit(1)
        filtered_data = filter_positive_numbers(sample_values)
        print(filtered_data)
    except TypeError as e:
        print(f"Validation error: {e}")