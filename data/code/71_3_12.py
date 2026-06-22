class ListAnalyzer:
    def __init__(self, items):
        self.items = list(items)

    def get_middle_value(self):
        count = len(self.items)
        if count == 0:
            return None
        if count % 2 == 1:
            return self.items[count // 2]
        left = self.items[count // 2 - 1]
        right = self.items[count // 2]
        return (left + right) / 2

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    analyzer = ListAnalyzer(sample_data)
    print(analyzer.get_middle_value())
    
    sample_data_even = [1, 2, 3, 4]
    analyzer_even = ListAnalyzer(sample_data_even)
    print(analyzer_even.get_middle_value())
    
    sample_data_single = [42]
    analyzer_single = ListAnalyzer(sample_data_single)
    print(analyzer_single.get_middle_value())