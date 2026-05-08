class SumCalculator:
    def __init__(self, numbers):
        self.numbers = numbers
    def calculate_sum(self):
        return sum(self.numbers)
if __name__ == '__main__':
    sample_list = [1, 5, 10, 2]
    calculator = SumCalculator(sample_list)
    total = calculator.calculate_sum()
    print(total)