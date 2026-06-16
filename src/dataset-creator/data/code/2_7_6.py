def positive_checker(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0 and args[0] <= 0:
            raise ValueError(f"Invalid input for {func.__name__}: The first argument must be a positive number. Received: {args[0]}")
        return func(*args, **kwargs)
    return wrapper
@positive_checker
def calculate_square(x):
    return x * x
if __name__ == '__main__':
    try:
        result = calculate_square(-5)
        print(f"Result for -5: {result}")
    except ValueError as e:
        print(e)
    try:
        result = calculate_square(0)
        print(f"Result for 0: {result}")
    except ValueError as e:
        print(e)
    try:
        result = calculate_square(10)
        print(f"Result for 10: {result}")
    except ValueError as e:
        print(e)