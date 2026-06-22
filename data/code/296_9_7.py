from fractions import Fraction

def add_ratios(ratio1, ratio2):
    return str(Fraction(ratio1) + Fraction(ratio2))

if __name__ == '__main__':
    print(add_ratios('1/2', '1/3'))