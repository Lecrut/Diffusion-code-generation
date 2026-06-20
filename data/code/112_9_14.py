class SumCalculator:
    def __init__(self, num1, num2):
        self.num1 = num1
        self.num2 = num2

    def get_sum(self):
        return self.num1 + self.num2

if __name__ == '__main__':
    calculator = SumCalculator(10, 5)
    print("Sum:", calculator.get_sum())