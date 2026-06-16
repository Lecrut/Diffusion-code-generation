def positive_checker(func):
    def wrapper(*args, **kwargs):
        if args and args[0] <= 0:
            raise ValueError(f"Invalid first argument {args[0]} for function '{func.__name__}'. The value must be a positive number.")
        return func(*args, **kwargs)
    return wrapper
@positive_checker
def calculate_sum(a, b):
    return a + b
if __name__ == '__main__':
    try:
        result = calculate_sum(-5, 10)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)
    try:
        result = calculate_sum(3.5, -2)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)
    try:
        result = calculate_sum(0, 10)
        print(f"Result: {result}")
    except ValueError as e:
        print(e)