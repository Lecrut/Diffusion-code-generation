def validate_first_argument(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0 and args[0] <= 100:
            raise ValueError("The first argument must be greater than 100.")
        return func(*args, **kwargs)
    return wrapper

@validate_first_argument
def compute_sum(x, y):
    return x + y

if __name__ == '__main__':
    try:
        result = compute_sum(200, 300)
        print(result)
    except ValueError as e:
        print(e)