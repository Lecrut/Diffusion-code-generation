import math

def calculate_simplified_ratio(num1, num2):
    gcd = math.gcd(num1, num2)
    return (num1 // gcd, num2 // gcd)

if __name__ == '__main__':
    sample_num1 = 108
    sample_num2 = 45
    simplified_ratio = calculate_simplified_ratio(sample_num1, sample_num2)
    print(simplified_ratio)