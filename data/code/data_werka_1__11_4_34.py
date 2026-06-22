from math import gcd

def calculate_simplified_ratio(num1, num2):
    common_divisor = gcd(num1, num2)
    simplified_numerator = num1 // common_divisor
    simplified_denominator = num2 // common_divisor
    return (simplified_numerator, simplified_denominator)

if __name__ == '__main__':
    numerator = 1000000000000
    denominator = 500000000000
    result = calculate_simplified_ratio(numerator, denominator)
    print(result)