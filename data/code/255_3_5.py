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
    analyzer.add_data(sample_data1)
    max1 = analyzer.get_maximum()
    print(f"Maximum of {sample_data1}: {max1}")
    sample_data2 = [3, 99, -5, 42]
    analyzer.add_data(sample_data2)
    max2 = analyzer.get_maximum()
    print(f"Maximum of {sample_data2}: {max2}")
    analyzer.add_data([1, 2, 3])
    max3 = analyzer.get_maximum()
    print(f"Maximum of the combined data: {max3}")
    empty_analyzer = DataAnalyzer()
    max4 = empty_analyzer.get_maximum()
    print(f"Maximum of empty data: {max4}")