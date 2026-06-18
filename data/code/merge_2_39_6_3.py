import sys
def find_largest_element(numbers):
    if not numbers:
        raise ValueError("Input list cannot be empty.")
    max_val = None
    for item in numbers:
        try:
            num = float(item)
            if max_val is not None and (num > max_val):
                max_val = num
        except ValueError:
            raise TypeError(f"Invalid data type encountered in input list: {type(item).__name__}. Only numeric values are allowed.")
    return max_val
if __name__ == '__main__':
    sample_data = [10, 25.5, "invalid", -3, float('inf'), 42]
    try:
        result = find_largest_element(sample_data)
        print(f"The largest element is: {result}")
    except (ValueError, TypeError):
        error_msg = sys.exc_info()[1].arg if isinstance(sys.exc_info()[1], ValueError or TypeError) else "An unexpected error occurred."
        print(error_msg)