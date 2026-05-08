def check_negative_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise ValueError("Function execution blocked: Return value is negative.")
        return result
    return wrapper
@check_negative_return
def multiply(a, b):
    return a * b
@check_negative_return
def add(a, b):
    return a + b
if __name__ == '__main__':
    print("Testing multiply:")
    try:
        result_mult_positive = multiply(5, 2)
        print(f"multiply(5, 2) = {result_mult_positive}")
        result_mult_negative = multiply(5, -2)
    except ValueError as e:
        print(f"Error caught for multiply: {e}")
    print("\nTesting add:")
    try:
        result_add_positive = add(10, 5)
        print(f"add(10, 5) = {result_add_positive}")
        result_add_negative = add(-10, 5)
    except ValueError as e:
        print(f"Error caught for add: {e}")