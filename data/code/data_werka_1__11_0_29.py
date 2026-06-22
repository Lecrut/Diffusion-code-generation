from math import gcd

def calculate_length_ratio(length_a, length_b):
    common_divisor = gcd(length_a, length_b)
    simplified_a = length_a // common_divisor
    simplified_b = length_b // common_divisor
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    sample_length_a = 240
    sample_length_b = 360
    result = calculate_length_ratio(sample_length_a, sample_length_b)
    print(result)