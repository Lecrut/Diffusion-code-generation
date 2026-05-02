def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result != 0:
            raise ValueError("Function result is not zero")
        return result
    return wrapper
@check_zero_result
def add(a, b):
    return a + b
if __name__ == '__main__':
    print(f"Test 1 (0 + 0): {add(0, 0)}")
    try:
        print(f"Test 2 (5 + -5): {add(5, -5)}")
    except ValueError as e:
        print(f"Test 2 Error: {e}")
    try:
        print(f"Test 3 (1 + 2): {add(1, 2)}")
    except ValueError as e:
        print(f"Test 3 Error: {e}")