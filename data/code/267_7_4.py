def length_check(max_length):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if 'input_string' in kwargs:
                input_str = kwargs['input_string']
                if len(input_str) > max_length:
                    raise ValueError(f"Input string length ({len(input_str)}) exceeds the maximum allowed length of {max_length}")
            else:
                pass
            return func(*args, **kwargs)
        return wrapper
    return decorator
@length_check(max_length=10)
def process_data(input_string, other_arg):
    return f"Processing string: {input_string}"
if __name__ == '__main__':
    print("--- Test Case 1: String within length limit ---")
    try:
        result1 = process_data(input_string="short", other_arg=123)
        print(result1)
    except ValueError as e:
        print(f"Error caught: {e}")
    print("\n--- Test Case 2: String exceeding length limit ---")
    try:
        result2 = process_data(input_string="this_is_way_too_long", other_arg=456)
        print(result2)
    except ValueError as e:
        print(f"Error caught: {e}")