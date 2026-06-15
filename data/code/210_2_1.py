class DataAnalyzer:
    def calculate_range(self, data):
        if not data:
            return None
        return max(data) - min(data)
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10, 20, 30, 40, 50]
    sample_data2 = [5, 2, 8, 1]
    sample_data3 = []
    range1 = analyzer.calculate_range(sample_data1)
    print(f"Range of {sample_data1}: {range1}")
    range2 = analyzer.calculate_range(sample_data2)
    print(f"Range of {sample_data2}: {range2}")
    range3 = analyzer.calculate_range(sample_data3)
    print(f"Range of {sample_data3}: {range3}")