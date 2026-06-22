class DataAnalyzer:
    def __init__(self):
        self.data_points = [3.14, 2.71, 1.41, 9.81, 4.67, 0.55, 7.23]

    def get_largest_data_point(self):
        largest = self.data_points[0]
        for value in self.data_points[1:]:
            if value > largest:
                largest = value
        return largest

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    result = analyzer.get_largest_data_point()
    print(result)