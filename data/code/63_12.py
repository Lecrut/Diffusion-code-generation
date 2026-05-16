class ListAnalyzer:
    def __init__(self, data):
        self.data = data
    def find_first_value(self):
        if self.data:
            return self.data[0]
        return None
if __name__ == '__main__':
    sample_list = [10, 20, 30, 40]
    analyzer = ListAnalyzer(sample_list)
    first = analyzer.find_first_value()
    print(first)
    sample_list_empty = []
    analyzer_empty = ListAnalyzer(sample_list_empty)
    first_empty = analyzer_empty.find_first_value()
    print(first_empty)