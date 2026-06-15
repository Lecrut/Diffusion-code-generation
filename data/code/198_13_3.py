class ListAnalyzer:
    def __init__(self, numbers):
        self._numbers = numbers
    def get_minimum(self):
        if not self._numbers:
            raise ValueError("The list cannot be empty")
        return min(self._numbers)
if __name__ == '__main__':
    sample_list = [3, 1, 4, 1, 5, 9, 2]
    analyzer = ListAnalyzer(sample_list)
    minimum_value = analyzer.get_minimum()
    print(minimum_value)