class NumberDifferenceCalculator:
    def __init__(self, num1: int, num2: int):
        self.num1 = num1
        self.num2 = num2

    def calculate_difference(self) -> int:
        return self.num1 - self.num2

if __name__ == '__main__':
    calculator = NumberDifferenceCalculator(34, 17)
    print(calculator.calculate_difference())