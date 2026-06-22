class NumberAnalyzer:
    MIN_NUMBER = -1e+308
    MAX_NUMBER = 1e+308

    def __init__(self, numbers):
        self.numbers = numbers

    @staticmethod
    def _validate_numbers(numbers):
        if not numbers:
            raise ValueError('The tuple must contain at least one number.')

    def find_difference(self):
        self._validate_numbers(self.numbers)
        return max(self.numbers) - min(self.numbers)
if __name__ == '__main__':
    sample_values = (3.5, 1.2, 4.8, 2.9)
    analyzer = NumberAnalyzer(sample_values)
    print(analyzer.find_difference())