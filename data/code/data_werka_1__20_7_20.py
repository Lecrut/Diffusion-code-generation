def check_eq(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError("Function must return a tuple with two elements")
        a, b = result
        if a != b:
            raise AssertionError(f"Strict equality check failed: {a} != {b}")
        return a, b
    return wrapper

@check_eq
def sample_function(x, y):
    return x, y

if __name__ == '__main__':
    try:
        print(sample_function(5, 5))
        print(sample_function('hello', 'world'))
    except (ValueError, AssertionError) as e:
        print(e)