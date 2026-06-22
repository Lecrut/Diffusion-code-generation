from fractions import Fraction

def simplify_ratio(numerator, denominator):
    return str(Fraction(numerator, denominator))
if __name__ == '__main__':
    result = simplify_ratio(45, 90)
    print(result)