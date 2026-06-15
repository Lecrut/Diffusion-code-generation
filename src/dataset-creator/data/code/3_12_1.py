class RatioCalculator:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    def calculate_ratio(self):
        if self.denominator == 0:
            raise ValueError("Denominator cannot be zero")
        return self.numerator / self.denominator
if __name__ == '__main__':
    num = 10
    den = 2
    calculator = RatioCalculator(num, den)
    ratio = calculator.calculate_ratio()
    print(ratio)