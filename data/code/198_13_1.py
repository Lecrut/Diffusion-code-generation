class ListAnalyzer:
    def __init__(self, numbers):
        self._numbers = numbers
    def get_minimum(self):
        if not self._numbers:
            raise ValueError("The list cannot be empty")
        return min(self._numbers)
if __name__ == '__main__':
    sample_list = [15, 3, 8, 22, 1]
    analyzer = ListAnalyzer(sample_list)
    minimum = analyzer.get_minimum()
    print(minimum)