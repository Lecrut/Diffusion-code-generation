from math import gcd

def calculate_length_ratio(length_a, length_b):
    common_divisor = gcd(length_a, length_b)
    simplified_a = length_a // common_divisor
    simplified_b = length_b // common_divisor
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    length_a = 120
    length_b = 180
    ratio = calculate_length_ratio(length_a, length_b)
    print(ratio)