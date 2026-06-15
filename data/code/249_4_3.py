class ListAnalyzer:
    def __init__(self, data):
        self._data = data
    def get_maximum(self):
        if not self._data:
            raise ValueError("The list is empty")
        maximum = self._data[0]
        for item in self._data[1:]:
            if item > maximum:
                maximum = item
        return maximum
if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 27]
    analyzer = ListAnalyzer(sample_list)
    maximum_value = analyzer.get_maximum()
    print(maximum_value)