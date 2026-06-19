from math import gcd

def calculate_length_ratio(length_a, length_b):
    common_divisor = gcd(length_a, length_b)
    return (length_a // common_divisor, length_b // common_divisor)

if __name__ == '__main__':
    length_a = 48
    length_b = 180
    ratio = calculate_length_ratio(length_a, length_b)
    print(ratio)