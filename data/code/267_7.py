def length_check(max_length):
    def decorator(func):
        def wrapper(*args):
            if args and isinstance(args[0], str) and len(args[0]) > max_length:
                raise ValueError(f"Input string exceeds maximum length of {max_length}")
            return func(*args)
        return wrapper
    return decorator
@length_check(10)
def process_string(input_str):
    return f"Processed: {input_str}"
if __name__ == '__main__':
    print(process_string("short"))
    try:
        process_string("this is too long")
    except ValueError as e:
        print(e)