def check_greater_than_constant(func):
    def wrapper(arg, *args, **kwargs):
        if arg <= 100:
            raise ValueError("Argument must be greater than 100")
        return func(arg, *args, **kwargs)
    return wrapper
@check_greater_than_constant
def decorated_function(x, y=1):
    return x + y
if __name__ == '__main__':
    try:
        result = decorated_function(101)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    try:
        result = decorated_function(50)
    except ValueError as e:
        print(f"Error: {e}")