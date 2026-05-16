import math
def evaluate_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else float('inf')
    return addition, subtraction, multiplication, division
if __name__ == '__main__':
    num1 = 10.0
    num2 = 3.0
    add, sub, mul, div = evaluate_operations(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Addition: {add}")
    print(f"Subtraction: {sub}")
    print(f"Multiplication: {mul}")
    print(f"Division: {div}")
    num3 = -5.5
    num4 = 2.0
    add2, sub2, mul2, div2 = evaluate_operations(num3, num4)
    print(f"\nNumber 3: {num3}")
    print(f"Number 4: {num4}")
    print(f"Addition: {add2}")
    print(f"Subtraction: {sub2}")
    print(f"Multiplication: {mul2}")
    print(f"Division: {div2}")