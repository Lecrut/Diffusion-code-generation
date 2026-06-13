class NumberAnalyzer:
    def __init__(self, numbers):
        self._numbers = numbers
    def get_maximum(self):
        if not self._numbers:
            raise ValueError("The list of numbers is empty")
        return max(self._numbers)
if __name__ == '__main__':
    sample_numbers = [15, 8, 42, 3, 99, 27]
    analyzer = NumberAnalyzer(sample_numbers)
    maximum_value = analyzer.get_maximum()
    print(maximum_value)