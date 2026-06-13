class NumberAnalyzer:
    def __init__(self, numbers):
        self._numbers = numbers
    def get_maximum(self):
        if not self._numbers:
            raise ValueError("The list of numbers is empty")
        return max(self._numbers)
if __name__ == '__main__':
    sample_numbers = [15, 8, 22, 4, 30, 11]
    analyzer = NumberAnalyzer(sample_numbers)
    maximum = analyzer.get_maximum()
    print(maximum)