def check_eq(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if not isinstance(result, tuple) or len(result) != 2:
            raise ValueError("Function must return a tuple with exactly two elements.")
        a, b = result
        if a != b:
            raise AssertionError(f"Strict equality check failed: {a} != {b}")
        return a, b
    return wrapper

@check_eq
def add_and_check(x, y):
    return x + y, 5

@check_eq
def multiply_and_check(x, y):
    return x * y, 10

if __name__ == '__main__':
    try:
        result_add = add_and_check(2, 3)
        print(f"Addition check: {result_add}")
        
        result_multiply = multiply_and_check(5, 2)
        print(f"Multiplication check: {result_multiply}")
    except (ValueError, AssertionError) as e:
        print(e)