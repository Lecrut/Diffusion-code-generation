import math
def evaluate_operations(a, b):
    addition = a + b
    subtraction = a - b
    multiplication = a * b
    division = a / b
    return addition, subtraction, multiplication, division
if __name__ == '__main__':
    num1 = 1.23456789e10
    num2 = 0.00000000123
    sum_val, diff_val, prod_val, quot_val = evaluate_operations(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print("-" * 30)
    print(f"Addition (a + b): {sum_val}")
    print(f"Subtraction (a - b): {diff_val}")
    print(f"Multiplication (a * b): {prod_val}")
    print(f"Division (a / b): {quot_val}")