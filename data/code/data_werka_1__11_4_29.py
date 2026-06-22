from math import gcd

def calculate_simplified_ratio(num1, num2):
    common_divisor = gcd(num1, num2)
    simplified_num = num1 // common_divisor
    simplified_denom = num2 // common_divisor
    return (simplified_num, simplified_denom)

if __name__ == '__main__':
    sample_num1 = 98
    sample_num2 = 42
    result = calculate_simplified_ratio(sample_num1, sample_num2)
    print(result)