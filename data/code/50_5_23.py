class NonNegativeDifferenceCalculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2

    def calculate(self):
        return abs(self.value1 - self.value2)

if __name__ == '__main__':
    calculator = NonNegativeDifferenceCalculator(30, 45)
    print(calculator.calculate())