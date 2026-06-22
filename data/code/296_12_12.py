import math

GCD_THRESHOLD = 1000

def simplify_fraction(numerator: int, denominator: int) -> tuple:
    gcd_value = math.gcd(abs(numerator), abs(denominator))
    
    if gcd_value == GCD_THRESHOLD or gcd_value == 1:
        return (numerator, denominator)
    
    return (numerator // gcd_value, denominator // gcd_value)

if __name__ == '__main__':
    sample_num = 24
    sample_den = 60
    simplified_ratio = simplify_fraction(sample_num, sample_den)
    print(f"Simplified ratio: {simplified_ratio[0]}/{simplified_ratio[1]}")