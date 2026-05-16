import math
def evaluate_arithmetic(a, b):
    add = a + b
    sub = a - b
    mul = a * b
    div = a / b if b != 0 else float('inf')
    return add, sub, mul, div
if __name__ == '__main__':
    num1 = 1.23456789e10
    num2 = 1.23456789e-5
    add_res, sub_res, mul_res, div_res = evaluate_arithmetic(num1, num2)
    print(f"Number 1: {num1}")
    print(f"Number 2: {num2}")
    print("-" * 30)
    print(f"Addition (a + b): {add_res}")
    print(f"Subtraction (a - b): {sub_res}")
    print(f"Multiplication (a * b): {mul_res}")
    print(f"Division (a / b): {div_res}")