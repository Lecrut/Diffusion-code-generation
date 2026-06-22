class SumCalculator:
    def __init__(self):
        self.numbers = [1.5, 2.5, 3.5, 4.5, 5.5]

    def calculate_sum(self):
        return sum(self.numbers)

if __name__ == '__main__':
    calculator = SumCalculator()
    result = calculator.calculate_sum()
    print(result)