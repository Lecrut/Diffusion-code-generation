class RatioCalculator:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator

    def calculate_ratio(self):
        if self.denominator != 0:
            return float(self.numerator) / self.denominator
        else:
            raise ValueError("Error: Division by zero")

if __name__ == '__main__':
    calculator = RatioCalculator(10, 4)
    result = calculator.calculate_ratio()
    print(f"Calculated Ratio: {result}")