def check_zero_result(func):
    def wrapper(*args, **kwargs):
        try:
            result = func(*args, **kwargs)
            if result == 0:
                print("The result is zero.")
            else:
                print(f"The result is not zero: {result}")
            return result
        except Exception as e:
            print(f"An error occurred: {e}")
            raise
    return wrapper

@check_zero_result
def add(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return a + b

@check_zero_result
def multiply(a, b):
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise ValueError("Both arguments must be numbers.")
    return a * b

if __name__ == '__main__':
    add(10, -10)
    add(4.5, 5.5)
    multiply(0, 10)
    try:
        add("a", "b")
    except ValueError as e:
        print(e)