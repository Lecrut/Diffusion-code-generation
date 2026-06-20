class SumCalculator:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c

    def calculate_sum(self):
        return sum((self.a, self.b, self.c))

if __name__ == '__main__':
    calculator = SumCalculator(10, 20, 30)
    result = calculator.calculate_sum()
    print(result)