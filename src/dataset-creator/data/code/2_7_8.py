def positive_checker(func):
    def wrapper(*args, **kwargs):
        if len(args) >= 1 and args[0] <= 0:
            raise ValueError(f"First argument must be a positive number, got {args[0]}")
        return func(*args, **kwargs)
    return wrapper
@positive_checker
def add_numbers(a, b):
    return a + b
if __name__ == '__main__':
    try:
        result = add_numbers(-5, 10)
    except ValueError as e:
        print(f"Error occurred: {e}")
    try:
        result = add_numbers(3.5, -2.5)
    except ValueError as e:
        print(f"Error occurred: {e}")
    try:
        result = add_numbers(10, 20)
        print(f"Success: {result}")
    except ValueError as e:
        print(f"Unexpected error: {e}")