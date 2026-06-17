def length_check(max_length):
    def decorator(func):
        def wrapper(*args):
            if args and isinstance(args[0], str) and len(args[0]) > max_length:
                raise ValueError(f"Input string exceeds maximum length of {max_length}")
            return func(*args)
        return wrapper
    return decorator
@length_check(10)
def process_string(text):
    return f"Processed: {text}"
if __name__ == '__main__':
    test_string_short = "hello"
    test_string_long = "this is a very long string"
    print(process_string(test_string_short))
    try:
        process_string(test_string_long)
    except ValueError as e:
        print(f"Error caught: {e}")