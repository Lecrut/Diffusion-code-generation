class NegativeResultError(Exception):
    pass
def check_negative(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise NegativeResultError("Function returned a negative result")
        return result
    return wrapper
@check_negative
def calculate_value(a, b):
    return a - b
if __name__ == '__main__':
    try:
        result = calculate_value(5, 10)
        print(f"Result: {result}")
    except NegativeResultError as e:
        print(f"Caught exception: {e}")
    try:
        result = calculate_value(10, 5)
        print(f"Result: {result}")
    except NegativeResultError as e:
        print(f"Caught exception: {e}")