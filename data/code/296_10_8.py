from fractions import Fraction

def simplify_ratio(numerator, denominator):
    return str(Fraction(numerator, denominator))

if __name__ == '__main__':
    print(simplify_ratio(4, 8))
    print(simplify_ratio(10, 25))