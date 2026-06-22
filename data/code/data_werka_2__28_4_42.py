def is_strictly_greater(func):
    def validate_args(a, b):
        if not (a > b):
            raise ValueError(f"The first argument {a} must be strictly greater than the second argument {b}.")
    
    def wrapper(*args, **kwargs):
        validate_args(args[0], args[1])
        return func(*args, **kwargs)
    
    return wrapper

@is_strictly_greater
def divide(a, b):
    return a / b

if __name__ == '__main__':
    try:
        result = divide(20, 5)
        print(result)
    except ValueError as e:
        print(e)

    try:
        result = divide(4, 8)
        print(result)
    except ValueError as e:
        print(e)