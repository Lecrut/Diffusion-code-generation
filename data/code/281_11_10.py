class SumCalculator:
    def __init__(self):
        self.values = [10, 20, 30, 40]

    def get_sum(self):
        return sum(self.values)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.get_sum()
    print(result)