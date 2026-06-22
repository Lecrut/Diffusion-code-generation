class SumCalculator:
    def __init__(self):
        self.value1 = 15
        self.value2 = 27

    def compute_sum(self):
        return self.value1 + self.value2

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.compute_sum()
    print(result)