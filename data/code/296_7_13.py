from math import gcd

def simplify_ratio(a, b):
    common_divisor = gcd(a, b)
    return (a // common_divisor, b // common_divisor)

def are_in_proportion(a, b, c, d):
    return a * d == b * c

def get_simplified_ratio(a, b, c, d):
    if not are_in_proportion(a, b, c, d):
        raise ValueError("Numbers are not in proportion")
    
    simplified_a = simplify_ratio(a, b)[0]
    simplified_b = simplify_ratio(a, b)[1]
    return (simplified_a, simplified_b)

if __name__ == '__main__':
    a_val = 8
    b_val = 4
    c_val = 6
    d_val = 3
    result = get_simplified_ratio(a_val, b_val, c_val, d_val)
    print(f"Simplified ratio is {result[0]}:{result[1]}")