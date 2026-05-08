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
        result1 = multiply(5, 3)
        print(f"multiply(5, 3) returned: {result1}")
        result2 = multiply(-5, 3)
        print(f"multiply(-5, 3) returned: {result2}")
    except ValueError as e:
        print(f"Error caught for multiply: {e}")
    print("\nTesting add:")
    try:
        result3 = add(10, 5)
        print(f"add(10, 5) returned: {result3}")
        result4 = add(-10, 5)
        print(f"add(-10, 5) returned: {result4}")
    except ValueError as e:
        print(f"Error caught for add: {e}")