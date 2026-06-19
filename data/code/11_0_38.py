def calculate_length_ratio(length_a, length_b):
    from math import gcd
    
    if length_a <= 0 or length_b <= 0:
        raise ValueError("Both lengths must be positive numbers.")
    
    common_divisor = gcd(int(length_a), int(length_b))
    simplified_ratio = (int(length_a) // common_divisor, int(length_b) // common_divisor)
    return simplified_ratio

if __name__ == '__main__':
    length_a = 18
    length_b = 24
    print(calculate_length_ratio(length_a, length_b))