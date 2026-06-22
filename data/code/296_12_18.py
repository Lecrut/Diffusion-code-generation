def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def simplify_fraction(num, den):
    common_divisor = gcd(num, den)
    simplified_num = num // common_divisor
    simplified_den = den // common_divisor
    return (simplified_num, simplified_den)

if __name__ == '__main__':
    initial_num = 36
    initial_den = 48
    simplified_fraction = simplify_fraction(initial_num, initial_den)
    print(f"Simplified fraction: {simplified_fraction[0]}/{simplified_fraction[1]}")