import math

def calculate_simplified_ratio(num1, num2):
    gcd = math.gcd(num1, num2)
    simplified_num = num1 // gcd
    simplified_den = num2 // gcd
    return (simplified_num, simplified_den)

if __name__ == '__main__':
    sample_num1 = 1000000000000000000000000000000
    sample_num2 = 400000000000000000000000000000
    result = calculate_simplified_ratio(sample_num1, sample_num2)
    print(result)