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
    print(f"Multiply 5 and 2: {multiply(5, 2)}")
    try:
        print(f"Multiply -5 and 2: {multiply(-5, 2)}")
    except ValueError as e:
        print(f"Error caught: {e}")
    print(f"Add 10 and 5: {add(10, 5)}")
    try:
        print(f"Add 10 and -5: {add(10, -5)}")
    except ValueError as e:
        print(f"Error caught: {e}")