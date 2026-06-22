def check_value(func):
    def wrapper(*args, **kwargs):
        if args[0] <= 100:
            raise ValueError("The first argument must be greater than 100")
        return func(*args, **kwargs)
    return wrapper

@check_value
def sample_function(value):
    return value * 2

if __name__ == '__main__':
    try:
        result = sample_function(150)
        print(result)
    except ValueError as e:
        print(e)