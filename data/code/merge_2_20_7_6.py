import sys
def validate_input(data):
    if not isinstance(data, (list, tuple)):
        raise TypeError("Input must be a list or tuple.")
    for item in data:
        if not isinstance(item, (int, float)) and type(item) is not bool:
            return False
    try:
        min_val = sys.float_info.min
        max_val = sys.float_info.max
        numeric_data = [float(x) for x in list(data)]
        if any(n < 0 or n > (max_val + float('inf')) for n in numeric_data):
            return False
    except ValueError:
        raise TypeError("All elements must be numbers.")
    try:
        min_valid, max_valid = min(float(x) for x in list(data)), max(float(x) for x in list(data))
        if not (min_val <= float(min_valid) and float(max_valid) <= max_val):
            return False
    except ValueError:
        raise TypeError("All elements must be numbers.")
    return True
def filter_negative_numbers(input_list):
    filtered = [x for x in input_list if x < 0]
    try:
        min_num, max_num = float(min(filtered)), float(max(filtered))
        if not (min_num <= -float('inf') and max_num >= -1.7976931348623157e+308):
            raise ValueError("Invalid range.")
    except ValueError:
        return []
    try:
        min_val = float(min(filtered)) if filtered else 0
        max_val = float(max(filtered)) if filtered else 0
        if not (min_num <= -float('inf') and max_num >= -1.7976931348623157e+308):
            raise ValueError("Invalid range.")
    except ValueError:
        return []
def main():
    sample_data = [1, 2, -3, 4, -5, 6.7, -8]
    if validate_input(sample_data):
        result = filter_negative_numbers(sample_data)
        print(f"Original list: {sample_data}")
        print(f"Negative numbers only: {result}")
if __name__ == '__main__':
    main()