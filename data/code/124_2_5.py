import math

def calculate_operations(a=25.5, b=4.2):
    sum_result = a + b
    difference_result = a - b
    product_result = a * b
    quotient_result = a / b if b != 0 else None
    power_result = math.pow(a, b)
    sqrt_result = math.sqrt(a) if a >= 0 else None

    return sum_result, difference_result, product_result, quotient_result, power_result, sqrt_result

if __name__ == '__main__':
    results = calculate_operations()
    print(results)