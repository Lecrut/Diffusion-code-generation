import math

def calculate_operations(a, b):
    sum_result = a + b
    difference = a - b
    product = a * b
    quotient = a / b if b != 0 else None
    remainder = a % b if b != 0 else None
    power = math.pow(a, b)
    square_root_a = math.sqrt(a) if a >= 0 else None
    square_root_b = math.sqrt(b) if b >= 0 else None
    return sum_result, difference, product, quotient, remainder, power, square_root_a, square_root_b

if __name__ == '__main__':
    result = calculate_operations(25.5, 4.2)
    print(result)