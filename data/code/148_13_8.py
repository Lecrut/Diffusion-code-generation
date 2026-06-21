class ListAnalyzer:
    def __init__(self, data):
        if not all(isinstance(item, (int, float)) for item in data):
            raise TypeError("All elements must be integers or floats")
        self._data = data

    def get_largest_element(self):
        if not self._data:
            raise ValueError("The list cannot be empty")
        largest = max(self._data)
        return largest

if __name__ == '__main__':
    sample_list = [15, 8, 42, 3, 99, 21]
    analyzer = ListAnalyzer(sample_list)
    largest = analyzer.get_largest_element()
    print(largest)