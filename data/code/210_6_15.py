class DataAnalyzer:
    def __init__(self, data):
        self.data = iter(data)

    def compute_range(self):
        try:
            min_val = max_val = next(self.data)
        except StopIteration:
            return 0

        for value in self.data:
            if value < min_val:
                min_val = value
            elif value > max_val:
                max_val = value

        return max_val - min_val

if __name__ == '__main__':
    analyzer = DataAnalyzer(x**2 for x in range(1000000))
    print(analyzer.compute_range())