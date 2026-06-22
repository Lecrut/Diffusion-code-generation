class SumCalculator:
    def __init__(self):
        self.numbers = [-10, -5, 0, 5, 10, 15]

    def calculate_sum(self):
        total = sum(self.numbers)
        return total

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum()
    print(f"Sum of (-10, -5, 0, 5, 10, 15): {result}")