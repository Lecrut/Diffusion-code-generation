import math

def calculate_simplified_ratio(num1, num2):
    gcd = math.gcd(num1, num2)
    simplified_num = num1 // gcd
    simplified_den = num2 // gcd
    return (simplified_num, simplified_den)

if __name__ == '__main__':
    sample_num1 = 48
    sample_num2 = 180
    result = calculate_simplified_ratio(sample_num1, sample_num2)
    print(result)