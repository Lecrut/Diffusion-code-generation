import math

def calculate_operations(a, b):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else None
    power_result = math.pow(a, b)
    sqrt_a = math.sqrt(a) if a >= 0 else None
    sqrt_b = math.sqrt(b) if b >= 0 else None

    return sum_result, difference_result, product_result, quotient_result, power_result, sqrt_a, sqrt_b

if __name__ == '__main__':
    result = calculate_operations(25.5, 4.2)
    print(result)