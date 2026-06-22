from fractions import Fraction

def add_ratios(ratio1: str, ratio2: str) -> str:
    f1 = Fraction(ratio1)
    f2 = Fraction(ratio2)
    result = f1 + f2
    return str(result)

if __name__ == '__main__':
    print(add_ratios("1/2", "1/3"))