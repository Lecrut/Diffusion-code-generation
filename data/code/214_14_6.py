class DataAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_min_value(self):
        return min(self.data)

if __name__ == '__main__':
    analyzer = DataAnalyzer([5, 3, 9, 1, 10])
    print(analyzer.find_min_value())