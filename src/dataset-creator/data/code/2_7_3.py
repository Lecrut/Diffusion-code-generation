def positive_checker(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0 and args[0] <= 0:
            raise ValueError(f"First argument must be a positive number. Received {args[0]}")
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