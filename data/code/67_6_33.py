class SumCalculator:
    def __init__(self, attr1, attr2):
        self.attr1 = attr1
        self.attr2 = attr2

    def calculate_sum(self):
        return self.attr1 + self.attr2

if __name__ == '__main__':
    calculator = SumCalculator(5, 7)
    print(calculator.calculate_sum())