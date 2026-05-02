import math
def calculate_length_ratio(length_a, length_b):
    if length_a == 0 or length_b == 0:
        raise ValueError("Lengths must be positive")
    common_divisor = math.gcd(length_a, length_b)
    return (length_a // common_divisor, length_b // common_divisor)
if __name__ == '__main__':
    print(calculate_length_ratio(12, 18))
    print(calculate_length_ratio(100, 75))
    print(calculate_length_ratio(7, 13))
    print(calculate_length_ratio(20, 5))