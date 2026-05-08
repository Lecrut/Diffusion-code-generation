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
    def regular_function(x):
        return x
    try:
        print(f"add(5, 3): {add(5, 3)}")
        print(f"multiply(2, 3): {multiply(2, 3)}")
        print(f"regular_function(10): {regular_function(10)}")
        result = regular_function(0)
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")
    except Exception as e:
        print(f"Caught unexpected exception: {e}")