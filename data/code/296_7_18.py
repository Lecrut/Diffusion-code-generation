def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_ratio(num1, den1, num2, den2):
    if num1 == 0 or den1 == 0 or num2 == 0 or den2 == 0:
        raise ValueError("All numbers must be non-zero.")
    
    common_divisor = gcd(gcd(num1, den1), gcd(num2, den2))
    return (num1 // common_divisor, den1 // common_divisor), (num2 // common_divisor, den2 // common_divisor)

if __name__ == '__main__':
    a_val = 4
    b_val = 8
    c_val = 6
    d_val = 12
    print(simplify_ratio(a_val, b_val, c_val, d_val))