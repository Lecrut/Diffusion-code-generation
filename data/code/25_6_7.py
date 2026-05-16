def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result != 0:
            raise ValueError("Function result is not zero")
        return result
    return wrapper
@check_zero_result
def multiply(a, b):
    return a * b
if __name__ == '__main__':
    print(f"Test 1 (0 * 5): {multiply(0, 5)}")
    try:
        print(f"Test 2 (2 * 0): {multiply(2, 0)}")
    except ValueError as e:
        print(f"Test 2 Error: {e}")
    try:
        print(f"Test 3 (2 * 3): {multiply(2, 3)}")
    except ValueError as e:
        print(f"Test 3 Error: {e}")