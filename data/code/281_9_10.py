class SumCalculator:
    def __init__(self):
        self.numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12}

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum()
    print(f"Sum of twelve numbers: {result}")