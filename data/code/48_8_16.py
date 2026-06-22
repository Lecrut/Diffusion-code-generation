class DataAnalyzer:
    def __init__(self):
        self.data_points = [3.14, 2.71, 1.41, 1.73, 0.577, 2.236]

    def get_largest_data_point(self):
        return max(self.data_points)

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    print(analyzer.get_largest_data_point())