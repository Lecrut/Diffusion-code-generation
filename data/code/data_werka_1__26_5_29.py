def check_first_arg(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0 and args[0] <= 100:
            raise ValueError("First argument must be greater than 100")
        return func(*args, **kwargs)
    return wrapper

@check_first_arg
def sample_function(arg1, arg2):
    return arg1 + arg2

if __name__ == '__main__':
    try:
        result = sample_function(50, 30)
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = sample_function(150, 30)
        print(result)
    except ValueError as e:
        print(e)