from math import gcd

def calculate_simplified_ratio(num1, num2):
    common_divisor = gcd(num1, num2)
    simplified_num = num1 // common_divisor
    simplified_den = num2 // common_divisor
    return (simplified_num, simplified_den)

if __name__ == '__main__':
    sample_num1 = 100
    sample_num2 = 75
    result = calculate_simplified_ratio(sample_num1, sample_num2)
    print(result)