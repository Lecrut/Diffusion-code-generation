class SumCalculator:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def calculate(self) -> int:
        return self.num1 + self.num2

if __name__ == '__main__':
    calculator = SumCalculator(4, 6)
    print(calculator.calculate())