class ListAnalyzer:
    def __init__(self, items):
        self.items = items

    def get_middle_value(self):
        count = len(self.items)
        if count == 0:
            return None
        if count == 1:
            return self.items[0]
        mid = count // 2
        if count % 2 == 1:
            return self.items[mid]
        return (self.items[mid - 1] + self.items[mid]) / 2

if __name__ == '__main__':
    analyzer = ListAnalyzer([10, 20, 30, 40, 50, 60])
    print(analyzer.get_middle_value())
    analyzer2 = ListAnalyzer([1, 2, 3])
    print(analyzer2.get_middle_value())
    analyzer3 = ListAnalyzer([42])
    print(analyzer3.get_middle_value())
    analyzer4 = ListAnalyzer([])
    print(analyzer4.get_middle_value())