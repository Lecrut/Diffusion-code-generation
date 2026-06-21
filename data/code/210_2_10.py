class DataAnalyzer:
    @staticmethod
    def calculate_range(data):
        if not data:
            return None
        minimum = min(data)
        maximum = max(data)
        return maximum - minimum

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10, 5, 20, 15]
    result1 = analyzer.calculate_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    sample_data2 = [3, 1, 4, 1, 5, 9, 2, 6]
    result2 = analyzer.calculate_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")
    sample_data3 = []
    result3 = analyzer.calculate_range(sample_data3)
    print(f"Data: {sample_data3}, Range: {result3}")