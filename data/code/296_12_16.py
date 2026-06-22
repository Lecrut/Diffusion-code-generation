def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(numerator, denominator):
    if not isinstance(numerator, int) or not isinstance(denominator, int):
        raise TypeError("Both numerator and denominator must be integers")
    if denominator == 0:
        raise ValueError("Denominator cannot be zero")
    
    common_divisor = gcd(numerator, denominator)
    return (numerator // common_divisor, denominator // common_divisor)

if __name__ == '__main__':
    sample_numerator = 12
    sample_denominator = 18
    simplified_fraction = simplify_fraction(sample_numerator, sample_denominator)
    print(f"Simplified fraction: {simplified_fraction[0]}/{simplified_fraction[1]}")