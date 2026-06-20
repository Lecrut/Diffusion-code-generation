class ArithmeticOperations:
    def __init__(self, num1: float, num2: float):
        self.num1 = num1
        self.num2 = num2

    def calculate_sum(self) -> float:
        return self.num1 + self.num2

    def calculate_difference(self) -> float:
        return self.num1 - self.num2

    def calculate_product(self) -> float:
        return self.num1 * self.num2

    def calculate_quotient(self) -> float:
        return self.num1 / self.num2

if __name__ == '__main__':
    op = ArithmeticOperations(10.5, 2.5)
    print(op.calculate_sum())
    print(op.calculate_difference())
    print(op.calculate_product())
    print(op.calculate_quotient())