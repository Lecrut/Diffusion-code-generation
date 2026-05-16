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
    print(multiply(5, 0))
    try:
        print(multiply(5, 2))
    except ValueError as e:
        print(f"Error: {e}")