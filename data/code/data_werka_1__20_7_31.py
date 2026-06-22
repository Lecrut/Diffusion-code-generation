def check_eq(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError("Function must return a tuple of two values to compare.")
        a, b = result
        if a != b:
            raise AssertionError(f"Strict equality check failed: {a} != {b}")
        return a, b
    return wrapper

@check_eq
def add_and_check(x, y):
    return x + y, 5

if __name__ == '__main__':
    try:
        result = add_and_check(2, 3)
        print(result)
    except AssertionError as e:
        print(e)