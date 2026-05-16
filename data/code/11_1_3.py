import math
def calculate_length_ratio(length_a, length_b):
    if length_b == 0:
        raise ValueError("Denominator cannot be zero")
    common_divisor = math.gcd(length_a, length_b)
    simplified_a = length_a // common_divisor
    simplified_b = length_b // common_divisor
    return (simplified_a, simplified_b)
if __name__ == '__main__':
    print(calculate_length_ratio(12, 18))
    print(calculate_length_ratio(100, 75))
    print(calculate_length_ratio(15, 5))
    print(calculate_length_ratio(7, 13))
    print(calculate_length_ratio(20, 40))