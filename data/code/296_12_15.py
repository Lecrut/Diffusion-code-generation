def simplify_fraction(fraction):
    num, den = fraction
    gcd = abs(num)
    while gcd > 1:
        if den % gcd == 0 and num % gcd == 0:
            break
        gcd -= 1
    return (num // gcd, den // gcd)

if __name__ == '__main__':
    initial_fraction = (12, 18)
    simplified_fraction = simplify_fraction(initial_fraction)
    print(f"Simplified fraction: {simplified_fraction[0]}/{simplified_fraction[1]}")