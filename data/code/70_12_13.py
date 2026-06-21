class SequenceAnalyzer:
    def __init__(self, data):
        if not data:
            raise ValueError("Input sequence must not be empty")
        self.data = data

    def get_boundaries(self):
        return self.data[0], self.data[-1]

if __name__ == '__main__':
    values = [42, 99, 13, 7, 55]
    analyzer = SequenceAnalyzer(values)
    first_item, last_item = analyzer.get_boundaries()
    print(first_item, last_item)