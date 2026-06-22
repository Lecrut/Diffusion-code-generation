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
def sample_function():
    return "Function executed"

@check_truth(False)
def blocked_function():
    return "This should not be printed"

if __name__ == '__main__':
    print(sample_function())
    print(blocked_function())