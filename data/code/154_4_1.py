class ListAnalyzer:
    def __init__(self, data):
        self._data = data
    def get_item_count(self):
        return len(self._data)
if __name__ == '__main__':
    sample_list = [1, 2, 3, 4, 5]
    analyzer = ListAnalyzer(sample_list)
    count = analyzer.get_item_count()
    print(count)