class MathOperations:
    def __init__(self, dividend=100, divisor=7):
        self.dividend = dividend
        self.divisor = divisor

    def calculate_quotient(self):
        return self.dividend // self.divisor

    def calculate_remainder(self):
        return self.dividend % self.divisor

if __name__ == '__main__':
    math_ops = MathOperations()
    quotient = math_ops.calculate_quotient()
    remainder = math_ops.calculate_remainder()
    print(f"Quotient: {quotient}")
    print(f"Remainder: {remainder}")