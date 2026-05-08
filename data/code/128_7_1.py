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
    print("Testing multiply(5, 2):")
    try:
        result = multiply(5, 2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting multiply(-5, 2):")
    try:
        result = multiply(-5, 2)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting add(10, -3):")
    try:
        result = add(10, -3)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")
    print("\nTesting add(10, -15):")
    try:
        result = add(10, -15)
        print(f"Result: {result}")
    except ValueError as e:
        print(f"Error: {e}")