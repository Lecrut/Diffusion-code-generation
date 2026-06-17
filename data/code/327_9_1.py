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
    num1 = 10
    num2 = 5
    print("--- Addition ---")
    result_add = add(num1, num2)
    print(f"{num1} + {num2} = {result_add}")
    print("\n--- Subtraction ---")
    result_sub = subtract(num1, num2)
    print(f"{num1} - {num2} = {result_sub}")
    print("\n--- Multiplication ---")
    result_mul = multiply(num1, num2)
    print(f"{num1} * {num2} = {result_mul}")
    print("\n--- Division ---")
    result_div = divide(num1, num2)
    print(f"{num1} / {num2} = {result_div}")
    num3 = 20
    num4 = 4
    print("\n--- Additional Examples ---")
    result_add_2 = add(num3, num4)
    print(f"{num3} + {num4} = {result_add_2}")
    result_sub_2 = subtract(num3, num4)
    print(f"{num3} - {num4} = {result_sub_2}")
    result_mul_2 = multiply(num3, num4)
    print(f"{num3} * {num4} = {result_mul_2}")
    result_div_2 = divide(num3, num4)
    print(f"{num3} / {num4} = {result_div_2}")
    try:
        divide(10, 0)
    except ZeroDivisionError as e:
        print(f"\nCaught expected error: {e}")