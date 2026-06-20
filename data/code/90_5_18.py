def or_condition_decorator(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not (result[0] or result[1]):
            raise ValueError("Function output does not satisfy 'or' condition")
        return result
    return wrapper

@or_condition_decorator
def example_function():
    return True, False

if __name__ == '__main__':
    try:
        print(example_function())
    except ValueError as e:
        print(e)