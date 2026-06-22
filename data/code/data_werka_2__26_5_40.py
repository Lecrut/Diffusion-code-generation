CONSTANT_THRESHOLD = 100

def check_first_arg_greater_than_100(func):
    def wrapper(*args, **kwargs):
        if len(args) > 0 and args[0] <= CONSTANT_THRESHOLD:
            raise ValueError("The first argument must be greater than 100.")
        return func(*args, **kwargs)
    return wrapper

@check_first_arg_greater_than_100
def add_numbers(a, b):
    return a + b

if __name__ == '__main__':
    try:
        result = add_numbers(150, 250)
        print(result)
    except ValueError as e:
        print(e)