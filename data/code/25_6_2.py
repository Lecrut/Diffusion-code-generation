def check_zero_result(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result != 0:
            raise ValueError("Function result was not zero")
        return result
    return wrapper
@check_zero_result
def my_function(a, b):
    return a + b
if __name__ == '__main__':
    print(my_function(5, -5))
    try:
        my_function(1, 2)
    except ValueError as e:
        print(f"Error caught: {e}")