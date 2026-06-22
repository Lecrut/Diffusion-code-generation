class DataAnalyzer:
    def __init__(self):
        self.data_points = [3.14, 2.71, 1.41, 1.73, 0.577]

    def compute_largest(self):
        return max(self.data_points)

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    result = analyzer.compute_largest()
    print(result)