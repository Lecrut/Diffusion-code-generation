def multiply_by_constant(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * factor
        return wrapper
    return decorator
@multiply_by_constant(5)
def double(x):
    return x * 2
@multiply_by_constant(10)
def add_ten(x):
    return x + 10
if __name__ == '__main__':
    print(double(3))
    print(add_ten(5))