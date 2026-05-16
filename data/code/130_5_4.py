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
    print("Testing add(5, 3):")
    try:
        result = add(5, 3)
        print(f"Result: {result}")
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")
    print("\nTesting multiply(2, 3):")
    try:
        result = multiply(2, 3)
        print(f"Result: {result}")
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")
    print("\nTesting regular_function(10):")
    try:
        result = regular_function(10)
        print(f"Result: {result}")
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")
    print("\nTesting function that returns zero directly:")
    @check_zero_return
    def return_zero():
        return 0
    try:
        return_zero()
    except ZeroReturnError as e:
        print(f"Caught exception: {e}")