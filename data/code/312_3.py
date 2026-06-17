class ListAnalyzer:
    def __init__(self, data):
        self._data = data
    def get_maximum(self):
        if not self._data:
            raise ValueError("The list is empty")
        return max(self._data)
if __name__ == '__main__':
    sample_list = [10, 5, 20, 8, 15]
    analyzer = ListAnalyzer(sample_list)
    maximum_value = analyzer.get_maximum()
    print(maximum_value)