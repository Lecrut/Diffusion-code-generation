def check_conditions(*conditions):
    def decorator(func):
        def wrapper(*args, **kwargs):
            result = func(*args, **kwargs)
            if not any(condition(result) for condition in conditions):
                raise ValueError(f"Function {func.__name__} returned {result}, which does not satisfy any of the required conditions.")
            return result
        return wrapper
    return decorator

@check_conditions(lambda x: x > 0, lambda x: x == 10)
def multiply(a, b):
    return a * b

if __name__ == '__main__':
    try:
        print(f"Test multiply(5, 2): {multiply(5, 2)}")
    except ValueError as e:
        print(e)

    try:
        print(f"Test multiply(-1, 3): {multiply(-1, 3)}")
    except ValueError as e:
        print(e)