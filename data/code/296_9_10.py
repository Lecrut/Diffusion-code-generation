from fractions import Fraction

class RatioCalculator:
    def __init__(self, ratio1, ratio2):
        self.ratio1 = Fraction(ratio1)
        self.ratio2 = Fraction(ratio2)

    def sum_ratios(self):
        return self.ratio1 + self.ratio2

if __name__ == '__main__':
    calculator = RatioCalculator('1/2', '3/4')
    result = calculator.sum_ratios()
    print(result)