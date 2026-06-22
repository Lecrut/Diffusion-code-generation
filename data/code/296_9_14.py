from fractions import Fraction

def add_ratios(ratio1: str, ratio2: str) -> str:
    return str(Fraction(ratio1) + Fraction(ratio2))

if __name__ == '__main__':
    result = add_ratios('1/2', '3/4')
    print(result)