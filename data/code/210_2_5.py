class DataAnalyzer:
    def calculate_range(self, data):
        if not data:
            return None
        minimum = min(data)
        maximum = max(data)
        return maximum - minimum
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10, 5, 20, 15]
    result1 = analyzer.calculate_range(sample_data1)
    print(f"Range of {sample_data1}: {result1}")
    sample_data2 = [3, 8, 1, 9, 4]
    result2 = analyzer.calculate_range(sample_data2)
    print(f"Range of {sample_data2}: {result2}")
    sample_data3 = [50]
    result3 = analyzer.calculate_range(sample_data3)
    print(f"Range of {sample_data3}: {result3}")
    sample_data4 = []
    result4 = analyzer.calculate_range(sample_data4)
    print(f"Range of {sample_data4}: {result4}")