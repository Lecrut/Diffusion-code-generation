def check_truth(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            return None
        return wrapper
    return decorator
@check_truth(True)
def greet(name):
    return f"Hello, {name}"
@check_truth(False)
def calculate(a, b):
    return a + b
if __name__ == '__main__':
    print(greet("World"))
    print(calculate(5, 10))