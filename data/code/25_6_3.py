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
    print(f"multiply(5, 0): {multiply(5, 0)}")
    try:
        print(f"multiply(5, 5): {multiply(5, 5)}")
    except ValueError as e:
        print(f"Error for multiply(5, 5): {e}")