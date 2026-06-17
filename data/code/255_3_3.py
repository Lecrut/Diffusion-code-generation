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
    sample_data1 = [10, 5, 20, 15]
    sample_data2 = [3, 8, 1, 9]
    analyzer.add_data(sample_data1)
    analyzer.add_data(sample_data2)
    maximum_value = analyzer.get_maximum()
    print(maximum_value)