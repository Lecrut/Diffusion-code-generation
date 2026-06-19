from math import gcd

def calculate_length_ratio(length_a, length_b):
    common_divisor = gcd(length_a, length_b)
    simplified_ratio = (length_a // common_divisor, length_b // common_divisor)
    return simplified_ratio

if __name__ == '__main__':
    sample_length_a = 18
    sample_length_b = 24
    result = calculate_length_ratio(sample_length_a, sample_length_b)
    print(result)