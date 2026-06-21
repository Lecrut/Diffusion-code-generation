def validate_first_argument(func):
    def wrapper(*args, **kwargs):
        MIN_VALUE = 100
        if args and args[0] <= MIN_VALUE:
            raise ValueError("The first argument must be greater than 100")
        return func(*args, **kwargs)
    return wrapper

@validate_first_argument
def compute_sum(arg1, arg2):
    return arg1 + arg2

if __name__ == '__main__':
    try:
        result = compute_sum(200, 300)
        print(result)
    except ValueError as e:
        print(e)