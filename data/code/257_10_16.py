class DifferenceCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_difference(self):
        return max(self.numbers) - min(self.numbers)

if __name__ == '__main__':
    sample_numbers = [10, 4, 25, 7, 5]
    calculator = DifferenceCalculator(sample_numbers)
    result = calculator.calculate_difference()
    print(result)