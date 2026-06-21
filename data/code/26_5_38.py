THRESHOLD = 100

def enforce_first_arg_greater_than_threshold(func):
    def wrapper(*args, **kwargs):
        if args and args[0] <= THRESHOLD:
            raise ValueError(f"The first argument must be greater than {THRESHOLD}")
        return func(*args, **kwargs)
    return wrapper

@enforce_first_arg_greater_than_threshold
def compute_sum(arg1, arg2):
    return arg1 + arg2

if __name__ == '__main__':
    try:
        result = compute_sum(200, 150)
        print(result)
    except ValueError as e:
        print(e)