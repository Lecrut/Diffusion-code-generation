def check_first_arg_greater_than_100(func):

    def wrapper(*args, **kwargs):
        if len(args) > 0 and args[0] <= 100:
            raise ValueError('The first argument must be greater than 100')
        return func(*args, **kwargs)
    return wrapper

@check_first_arg_greater_than_100
def sample_function(x, y):
    return x + y
if __name__ == '__main__':
    try:
        result = sample_function(150, 200)
        print(result)
    except ValueError as e:
        print(e)
    try:
        result = sample_function(50, 200)
        print(result)
    except ValueError as e:
        print(e)