def calculate_length_ratio(length_a, length_b):
    from math import gcd
    
    common_divisor = gcd(length_a, length_b)
    simplified_a = length_a // common_divisor
    simplified_b = length_b // common_divisor
    
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    ratio = calculate_length_ratio(180, 45)
    print(ratio)