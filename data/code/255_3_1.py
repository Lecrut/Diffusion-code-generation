class DataAnalyzer:
    def __init__(self):
        self.data = []
    def add_data(self, data_list):
        self.data.extend(data_list)
    def get_maximum(self):
        if not self.data:
            return None
        return max(self.data)
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10, 5, 22, 8]
    sample_data2 = [30, 15, 40, 25]
    analyzer.add_data(sample_data1)
    print(f"Maximum of data set 1: {analyzer.get_maximum()}")
    analyzer.add_data(sample_data2)
    print(f"Maximum of data set 2: {analyzer.get_maximum()}")
    analyzer.add_data([1, 50, 3])
    print(f"Maximum of combined data: {analyzer.get_maximum()}")
    empty_analyzer = DataAnalyzer()
    print(f"Maximum of empty data set: {empty_analyzer.get_maximum()}")