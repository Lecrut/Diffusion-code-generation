import sys
def find_max_value(numbers):
    sanitized_numbers = sanitize_input(numbers)
    if not sanitized_numbers:
        raise ValueError("Input list cannot be empty.")
    max_val = sanitized_numbers[0]
    for num in sanitized_numbers[1:]:
        try:
            numeric_value = float(num)
            if numeric_value > max_val:
                max_val = numeric_value
        except (TypeError, ValueError):
            raise TypeError(f"Invalid number format found: {num}")
    return int(max_val)
def sanitize_input(input_list):
    cleaned_list = []
    for item in input_list:
        if isinstance(item, (int, float)):
            cleaned_list.append(float(item))
        elif isinstance(item, str):
            try:
                cleaned_list.append(float(item.strip()))
            except ValueError:
                raise TypeError(f"Cannot convert '{item}' to a number.")
    return [x for x in cleaned_list if not (isinstance(x, float) and (float('inf') <= x or x < float('-inf')))]
def report_error(error_type):
    messages = {
        ValueError: "ValueError: Invalid input data provided.",
        TypeError: f"TypeError: Expected numeric input, got invalid format."
    }
    if error_type in messages:
        print(messages[error_type])
        sys.exit(1)
    raise error_type
if __name__ == '__main__':
    sample_data = [3.5, "7", None, 2, -4]
    try:
        result = find_max_value(sample_data)
        print(f"Maximum value found: {result}")
    except Exception as e:
        report_error(type(e))