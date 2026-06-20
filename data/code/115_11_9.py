class MathOperations:
    def __init__(self, dividend, divisor):
        self.dividend = dividend
        self.divisor = divisor

    def calculate_quotient(self):
        return self.dividend // self.divisor

    def calculate_remainder(self):
        return self.dividend % self.divisor

if __name__ == '__main__':
    math_ops = MathOperations(100, 7)
    quotient = math_ops.calculate_quotient()
    remainder = math_ops.calculate_remainder()
    print(f"Quotient of {math_ops.dividend} // {math_ops.divisor}: {quotient}")
    print(f"Remainder of {math_ops.dividend} % {math_ops.divisor}: {remainder}")