from fractions import Fraction

def add_ratios(ratio1, ratio2):
    return (Fraction(ratio1) + Fraction(ratio2)).limit_denominator()

if __name__ == '__main__':
    result = add_ratios('1/2', '3/4')
    print(result)