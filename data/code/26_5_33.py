THRESHOLD = 100

def check_first_arg_greater_than_threshold(func):
    def wrapper(*args, **kwargs):
        if args and args[0] <= THRESHOLD:
            raise ValueError("The first argument must be greater than 100")
        return func(*args, **kwargs)
    return wrapper

@check_first_arg_greater_than_threshold
def sample_function(arg1, arg2):
    return arg1 + arg2

if __name__ == '__main__':
    try:
        result = sample_function(150, 200)
        print(result)
    except ValueError as e:
        print(e)