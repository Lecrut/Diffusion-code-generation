class DataAnalyzer:
    def __init__(self):
        self.data = [3.5, 7.2, 1.8, 9.4, 6.1, 4.3]

    def get_largest_value(self):
        if not self.data:
            return None
        largest = self.data[0]
        for value in self.data:
            if value > largest:
                largest = value
        return largest

if __name__ == "__main__":
    analyzer = DataAnalyzer()
    print(analyzer.get_largest_value())