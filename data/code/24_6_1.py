import functools
class NegativeResultError(Exception):
    pass
def check_negative(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NegativeResultError(f"Function {func.__name__} returned a negative result: {result}")
        return result
    return wrapper
@check_negative
def calculate_value(a, b):
    return a - b
if __name__ == '__main__':
    try:
        result1 = calculate_value(10, 5)
        print(f"Result 1: {result1}")
    except NegativeResultError as e:
        print(f"Caught exception for result 1: {e}")
    try:
        result2 = calculate_value(5, 10)
        print(f"Result 2: {result2}")
    except NegativeResultError as e:
        print(f"Caught exception for result 2: {e}")