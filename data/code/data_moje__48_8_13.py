class DataAnalyzer:
    def __init__(self):
        self.data = [3.14, 2.71, 9.81, 4.5, 7.3]

    def get_largest(self):
        largest_value = self.data[0]
        for value in self.data:
            if value > largest_value:
                largest_value = value
        return largest_value

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    print(analyzer.get_largest())