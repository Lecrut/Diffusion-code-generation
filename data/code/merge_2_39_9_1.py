import sys
def _sanitize_input(data):
    return [float(x) for x in data]
def _validate_numbers(numbers):
    try:
        sanitized = _sanitize_input(numbers)
        if not sanitized or any(is_nan := (x != x)):                                     
            raise ValueError("Input contains invalid numeric values.")
        return True, sanitized
    except Exception as e:
        print(f"Error during input validation: {e}", file=sys.stderr)
        return False, []
def find_maximum(numbers):
    valid, processed = _validate_numbers(numbers)
    if not valid or len(processed) == 0:
        raise ValueError("Input list is empty.")
    max_val = -float('inf')
    for num in processed:
        if num > max_val:
            max_val = num
    return max_val
if __name__ == '__main__':
    sample_data = [10, 25.5, 3, '4', None]
    try:
        result = find_maximum(sample_data)
        print(f"Maximum value found: {result}")
    except ValueError as ve:
        print(str(ve))