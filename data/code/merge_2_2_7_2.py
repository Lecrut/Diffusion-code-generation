def positive_checker(func):
    def wrapper(*args, **kwargs):
        if args and not isinstance(args[0], (int, float)) or args[0] <= 0:
            raise ValueError(f"Invalid input for {func.__name__}: First argument must be a positive number. Received: {args[0]}")
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
print(calculate_sum(10, 20))