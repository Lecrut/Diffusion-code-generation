class ListAnalyzer:
    def __init__(self, data):
        if not all(isinstance(x, (int, float)) for x in data):
            raise ValueError("All elements must be numbers")
        self._data = data
    
    def get_maximum(self):
        return max(self._data)

if __name__ == '__main__':
    sample_list = [10, 5, 42, 3, 99, 21]
    analyzer = ListAnalyzer(sample_list)
    maximum_value = analyzer.get_maximum()
    print(maximum_value)