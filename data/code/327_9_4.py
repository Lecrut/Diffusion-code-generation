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
    print("Testing add function:")
    result_add = add(10, 5)
    print(f"10 + 5 = {result_add}")
    print("\nTesting subtract function:")
    result_subtract = subtract(20, 7)
    print(f"20 - 7 = {result_subtract}")
    print("\nTesting multiply function:")
    result_multiply = multiply(6, 8)
    print(f"6 * 8 = {result_multiply}")
    print("\nTesting divide function:")
    result_divide = divide(100, 4)
    print(f"100 / 4 = {result_divide}")
    try:
        result_divide_error = divide(10, 0)
    except ZeroDivisionError as e:
        print(f"\nCaught expected error for division by zero: {e}")