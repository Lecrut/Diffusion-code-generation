def length_check(max_length):
    def decorator(func):
        def wrapper(*args):
            if len(args) > max_length:
                raise ValueError("Input argument exceeds the maximum allowed length.")
            return func(*args)
        return wrapper
    return decorator
@length_check(5)
def process_string(s):
    return f"Processed: {s}"
if __name__ == '__main__':
    try:
        print(process_string("short"))
        print(process_string("longerstring"))
    except ValueError as e:
        print(f"Error caught: {e}")