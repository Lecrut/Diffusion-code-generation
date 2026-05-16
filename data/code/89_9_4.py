import math
def evaluate_arithmetic_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b if b != 0 else float('inf')
    return addition, subtraction, multiplication, division
if __name__ == '__main__':
    num1 = 10.0
    num2 = 3.0
    sum_val, diff_val, prod_val, div_val = evaluate_arithmetic_operations(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print(f"Addition: {sum_val}")
    print(f"Subtraction: {diff_val}")
    print(f"Multiplication: {prod_val}")
    print(f"Division: {div_val}")
    num3 = -5.5
    num4 = 2.0
    sum_val2, diff_val2, prod_val2, div_val2 = evaluate_arithmetic_operations(num3, num4)
    print(f"\nNumber 3: {num3}")
    print(f"Number 4: {num4}")
    print(f"Addition: {sum_val2}")
    print(f"Subtraction: {diff_val2}")
    print(f"Multiplication: {prod_val2}")
    print(f"Division: {div_val2}")