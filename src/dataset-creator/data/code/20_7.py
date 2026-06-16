def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        if not isinstance(item, int) and not isinstance(item, float):
            return False
    return True
def filter_negative_numbers(numbers):
    result = []
    for num in numbers:
        if num < 0:
            result.append(num)
    return result
if __name__ == '__main__':
    sample_data = [1, -5, 3.7, -2, "error", -9]
    try:
        is_valid = validate_input(sample_data)
        if not is_valid:
            print("Invalid input detected.")
        else:
            filtered_list = filter_negative_numbers(sample_data)
            print(filtered_list)
    except TypeError as e:
        print(f"Error: {e}")