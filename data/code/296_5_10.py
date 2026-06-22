from fractions import Fraction

def multiply_fractions(frac1, frac2):
    return frac1 * frac2

if __name__ == '__main__':
    result = multiply_fractions(Fraction(1, 2), Fraction(3, 4))
    print(result)