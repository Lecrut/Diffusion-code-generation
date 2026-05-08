class ListAnalyzer:
    def __init__(self, data):
        self._data = data
    def get_largest_element(self):
        if not self._data:
            raise ValueError("The list cannot be empty")
        largest = self._data[0]
        for element in self._data[1:]:
            if element > largest:
                largest = element
        return largest
if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 21]
    analyzer = ListAnalyzer(sample_list)
    largest = analyzer.get_largest_element()
    print(largest)