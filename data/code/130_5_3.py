import functools
class ZeroReturnError(Exception):
    pass
def check_zero_return(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result == 0:
            raise ZeroReturnError("Function returned zero")
        return result
    return wrapper
if __name__ == '__main__':
    @check_zero_return
    def add(a, b):
        return a + b
    @check_zero_return
    def multiply(a, b):
        return a * b
    def subtract(a, b):
        return a - b
    try:
        print(f"add(5, 3) = {add(5, 3)}")
        print(f"multiply(4, 0) = {multiply(4, 0)}")
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")
    try:
        print(f"subtract(5, 5) = {subtract(5, 5)}")
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")