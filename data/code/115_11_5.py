class DivisionCalculator:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def calculate_quotient(self):
        if self.divisor == 0:
            raise ValueError("Cannot divide by zero")
        return self.dividend // self.divisor

    def calculate_remainder(self):
        if self.divisor == 0:
            raise ValueError("Cannot divide by zero")
        return self.dividend % self.divisor

if __name__ == '__main__':
    calc = DivisionCalculator(100, 7)
    quotient = calc.calculate_quotient()
    remainder = calc.calculate_remainder()
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")