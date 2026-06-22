def calculate_length_ratio(length_a, length_b):
    from math import gcd
    
    common_divisor = gcd(int(length_a), int(length_b))
    simplified_ratio = (int(length_a) // common_divisor, int(length_b) // common_divisor)
    return simplified_ratio

if __name__ == '__main__':
    length_a = 120
    length_b = 75
    result = calculate_length_ratio(length_a, length_b)
    print(result)