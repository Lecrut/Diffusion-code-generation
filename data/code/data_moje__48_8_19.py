class DataAnalyzer:
    def __init__(self):
        self.data_points = [3.14, 2.71, 1.41, 1.73, 0.577, 2.236, 1.618]

    def get_largest_data_point(self):
        largest = self.data_points[0]
        for point in self.data_points[1:]:
            if point > largest:
                largest = point
        return largest

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    result = analyzer.get_largest_data_point()
    print(result)