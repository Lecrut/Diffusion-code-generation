def require_or(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not condition(result):
                raise AssertionError(f"Function {func.__name__} returned {result}, which does not satisfy the required condition.")
            return result
        return wrapper
    return decorator
@require_or(lambda x: x > 0)
def multiply(a, b):
    return a * b
@require_or(lambda x: x == 10)
def get_ten():
    return 10
@require_or(lambda x: x % 2 == 0)
def double(x):
    return x * 2
if __name__ == '__main__':
    print(f"multiply(5, 2): {multiply(5, 2)}")
    print(f"get_ten(): {get_ten()}")
    print(f"double(4): {double(4)}")
    try:
        multiply(0, 5)
    except AssertionError as e:
        print(f"Caught expected error for multiply(0, 5): {e}")