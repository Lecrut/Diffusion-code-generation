from math import gcd

def calculate_simplified_ratio(num1, num2):
    if not isinstance(num1, int) or not isinstance(num2, int):
        raise ValueError("Both inputs must be integers.")
    if num2 == 0:
        raise ValueError("Denominator cannot be zero.")
    
    common_divisor = gcd(num1, num2)
    simplified_num = num1 // common_divisor
    simplified_den = num2 // common_divisor
    return (simplified_num, simplified_den)

if __name__ == '__main__':
    sample_num1 = 9876543210987654321
    sample_num2 = 1234567890123456789
    try:
        result = calculate_simplified_ratio(sample_num1, sample_num2)
        print(result)
    except ValueError as e:
        print(e)