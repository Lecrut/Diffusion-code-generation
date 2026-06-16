def add(a, b):
    return a + b
def subtract(a, b):
    return a - b
def multiply(a, b):
    return a * b
def divide(a, b):
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
if __name__ == '__main__':
    print("--- Testing Addition ---")
    num1 = 10
    num2 = 5
    result_add = add(num1, num2)
    print(f"Addition of {num1} and {num2}: {result_add}")
    print("\n--- Testing Subtraction ---")
    num3 = 15
    num4 = 7
    result_sub = subtract(num3, num4)
    print(f"Subtraction of {num3} and {num4}: {result_sub}")
    print("\n--- Testing Multiplication ---")
    num5 = 6
    num6 = 8
    result_mul = multiply(num5, num6)
    print(f"Multiplication of {num5} and {num6}: {result_mul}")
    print("\n--- Testing Division ---")
    num7 = 20
    num8 = 4
    result_div = divide(num7, num8)
    print(f"Division of {num7} by {num8}: {result_div}")
    print("\n--- Testing Division by Zero (Error Handling) ---")
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        print(f"Caught expected error: {e}")