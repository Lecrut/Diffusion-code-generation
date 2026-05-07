import functools
def or_test(condition):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not condition(result):
                raise AssertionError(f"Function {func.__name__} returned {result}, which does not satisfy the required condition.")
            return result
        return wrapper
    return decorator
@or_test(lambda x: x > 0)
def multiply(a, b):
    return a * b
@or_test(lambda x: x == 10)
def add_ten(x):
    return x + 10
if __name__ == '__main__':
    print("Testing multiply(5, 2):")
    try:
        result = multiply(5, 2)
        print(f"Result: {result}")
    except AssertionError as e:
        print(f"Test Failed: {e}")
    print("\nTesting add_ten(0):")
    try:
        result = add_ten(0)
        print(f"Result: {result}")
    except AssertionError as e:
        print(f"Test Failed: {e}")