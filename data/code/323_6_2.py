import functools
def calculate_difference(constant_value):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result - constant_value
        return wrapper
    return decorator
@calculate_difference(constant_value=10)
def add(a, b):
    return a + b
if __name__ == '__main__':
    result = add(5, 3)
    print(result)