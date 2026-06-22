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

if __name__ == '__main__':
    result = sample_function()
    print(result)