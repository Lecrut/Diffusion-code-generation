class DataAnalyzer:
    def __init__(self):
        self.data_points = [3.14, 2.71, 1.41, 9.8, 5.5, 7.2]

    def get_largest_data_point(self):
        return max(self.data_points)

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    largest = analyzer.get_largest_data_point()
    print(largest)