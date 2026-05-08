class ListAnalyzer:
    def __init__(self, numbers):
        self._numbers = numbers
    def get_average(self):
        if not self._numbers:
            return 0
        return sum(self._numbers) / len(self._numbers)
if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    analyzer = ListAnalyzer(sample_data)
    average = analyzer.get_average()
    print(average)