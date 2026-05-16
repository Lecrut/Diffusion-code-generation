class ListAnalyzer:
    def __init__(self, data):
        self._data = list(data)
    def get_average(self):
        if not self._data:
            return 0
        return sum(self._data) / len(self._data)
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40, 50]
    analyzer = ListAnalyzer(sample_list)
    average = analyzer.get_average()
    print(average)