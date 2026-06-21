class SumCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_sum(self):
        return sum(self.data)

if __name__ == '__main__':
    calculator = SumCalculator([1, 2, 3, 4, 5])
    total = calculator.calculate_sum()
    print("Total sum:", total)