def calculate_difference(constant):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            return result - constant
        return wrapper
    return decorator
@calculate_difference(constant=10)
def add(a, b):
    return a + b
if __name__ == '__main__':
    print(add(5, 3))