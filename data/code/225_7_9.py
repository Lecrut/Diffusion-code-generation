class ValueAnalyzer:
    def __init__(self, tuple1, tuple2):
        self.values = tuple1 + tuple2

    def get_min(self):
        return min(self.values)

    def get_max(self):
        return max(self.values)

if __name__ == '__main__':
    sample_tuple1 = (5, 9, 3)
    sample_tuple2 = (8, 1, 7)
    analyzer = ValueAnalyzer(sample_tuple1, sample_tuple2)
    print(f"Minimum: {analyzer.get_min()}")
    print(f"Maximum: {analyzer.get_max()}")