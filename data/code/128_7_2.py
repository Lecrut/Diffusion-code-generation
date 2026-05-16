def check_negative_return(func):
    def wrapper(*args, **kwargs):
        result = func(*args, **kwargs)
        if result < 0:
            raise ValueError("Function returned a negative value, execution blocked.")
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
        result_mult = multiply(5, 2)
        print(f"multiply(5, 2) = {result_mult}")
        result_mult_neg = multiply(-5, 2)
    except ValueError as e:
        print(f"Error caught for multiply: {e}")
    print("\nTesting add:")
    try:
        result_add = add(10, 5)
        print(f"add(10, 5) = {result_add}")
        result_add_neg = add(10, -5)
    except ValueError as e:
        print(f"Error caught for add: {e}")