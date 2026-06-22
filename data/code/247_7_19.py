class SumCalculator:
    def __init__(self):
        self.CONSTANT_A = 5
        self.CONSTANT_B = 3

    def calculate_sum(self):
        return self.CONSTANT_A + self.CONSTANT_B

if __name__ == '__main__':
    calculator = SumCalculator()
    print(calculator.calculate_sum())