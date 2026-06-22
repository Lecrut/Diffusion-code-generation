class ListAnalyzer:

    def __init__(self, data):
        self.data = data

    def find_last_index(self, target):
        return self.data[::-1].index(target) if target in self.data else -1
if __name__ == '__main__':
    analyzer = ListAnalyzer([10, 20, 30, 40, 50, 40])
    print(analyzer.find_last_index(40))
    print(analyzer.find_last_index(60))