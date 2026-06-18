def multiply(factor):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result * factor
        return wrapper
    return decorator
@multiply(5)
def add(a, b):
    return a + b
if __name__ == '__main__':
    result = add(3, 4)
    print(result)