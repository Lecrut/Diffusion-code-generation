class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def get_middle_value(self):
        if not self.data:
            raise ValueError("List is empty")
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            mid = n // 2
            return (self.data[mid - 1] + self.data[mid]) / 2

if __name__ == '__main__':
    analyzer = ListAnalyzer([1, 2, 3, 4, 5])
    print(analyzer.get_middle_value())
    analyzer2 = ListAnalyzer([1, 2, 3, 4])
    print(analyzer2.get_middle_value())