import math

def calculate_operations(a, b):
    add = a + b
    subtract = a - b
    multiply = a * b
    divide = a / b if b != 0 else None
    power = math.pow(a, b)
    sqrt_a = math.sqrt(a) if a >= 0 else None
    sqrt_b = math.sqrt(b) if b >= 0 else None

    return add, subtract, multiply, divide, power, sqrt_a, sqrt_b

if __name__ == '__main__':
    result = calculate_operations(25.5, 4.2)
    print(result)