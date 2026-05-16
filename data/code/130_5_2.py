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
    def func1(a, b):
        return a + b
    @check_zero_return
    def func2(x):
        return 0
    @check_zero_return
    def func3(y, z):
        return y * z
    print("Testing func1(5, 3):")
    try:
        result1 = func1(5, 3)
        print(f"Result: {result1}")
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")
    print("\nTesting func2(10):")
    try:
        result2 = func2(10)
        print(f"Result: {result2}")
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")
    print("\nTesting func3(4, 5):")
    try:
        result3 = func3(4, 5)
        print(f"Result: {result3}")
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")