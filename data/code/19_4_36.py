def check_truth(condition):
    def decorator(func):
        def wrapper(*args, **kwargs):
            if condition:
                return func(*args, **kwargs)
            else:
                raise ValueError("Condition is not met")
        return wrapper
    return decorator

@check_truth(True)
def example_function():
    return "Function executed"

if __name__ == '__main__':
    try:
        result = example_function()
        print(result)
    except ValueError as e:
        print(e)