def check_truth(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                raise ValueError("Condition not met")
        return wrapper
    return decorator

@check_truth(True)
def sample_function():
    return "Function executed"

if __name__ == '__main__':
    try:
        result = sample_function()
        print(result)
    except ValueError as e:
        print(e)