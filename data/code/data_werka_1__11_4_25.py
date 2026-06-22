from math import gcd

def calculate_simplified_ratio(num1, num2):
    common_divisor = gcd(num1, num2)
    simplified_num1 = num1 // common_divisor
    simplified_num2 = num2 // common_divisor
    return (simplified_num1, simplified_num2)

if __name__ == '__main__':
    sample_num1 = 100
    sample_num2 = 45
    result = calculate_simplified_ratio(sample_num1, sample_num2)
    print(result)