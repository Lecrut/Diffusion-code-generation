class DataAnalyzer:
    def calculate_range(self, data):
        if not data:
            return None
        minimum = min(data)
        maximum = max(data)
        return maximum - minimum
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10, 25, 32, 8, 40]
    result1 = analyzer.calculate_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    sample_data2 = [5, 5, 5, 5]
    result2 = analyzer.calculate_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")
    sample_data3 = []
    result3 = analyzer.calculate_range(sample_data3)
    print(f"Data: {sample_data3}, Range: {result3}")
    sample_data4 = [100, 0, -50]
    result4 = analyzer.calculate_range(sample_data4)
    print(f"Data: {sample_data4}, Range: {result4}")