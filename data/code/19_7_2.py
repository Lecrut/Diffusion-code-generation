def check_truth(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                return None
        return wrapper
    return decorator
@check_truth(True)
def greet(name):
    return f"Hello, {name}"
@check_truth(False)
def secret_action(data):
    return f"Secret action executed with: {data}"
if __name__ == '__main__':
    print(greet("World"))
    print(secret_action("Sensitive Data"))