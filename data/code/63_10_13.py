class ListAnalyzer:
    def __init__(self, data):
        self.data = data

    def find_first_value(self):
        if not self.data:
            return None
        return self.data[0]

if __name__ == '__main__':
    sample_list = [42, 7, 19, 3]
    analyzer = ListAnalyzer(sample_list)
    print(analyzer.find_first_value())