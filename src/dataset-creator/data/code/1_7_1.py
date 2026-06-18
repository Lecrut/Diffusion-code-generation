def subtract_decorator(constant_value):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result - constant_value
        return wrapper
    return decorator
@subtract_decorator(5)
def sample_subtraction(a, b):
    return a - b
if __name__ == '__main__':
    x = 10
    y = 3
    result = sample_subtraction(x, y)
    print(result)