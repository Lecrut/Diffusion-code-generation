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
    print("Testing multiply with positive inputs:")
    try:
        result_mul = multiply(5, 3)
        print(f"multiply(5, 3) = {result_mul}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting multiply with inputs resulting in a negative value:")
    try:
        result_mul_neg = multiply(5, -1)
        print(f"multiply(5, -1) = {result_mul_neg}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting add with positive inputs:")
    try:
        result_add = add(10, 5)
        print(f"add(10, 5) = {result_add}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting add with inputs resulting in a negative value:")
    try:
        result_add_neg = add(10, -15)
        print(f"add(10, -15) = {result_add_neg}")
    except ValueError as e:
        print(f"Error: {e}")