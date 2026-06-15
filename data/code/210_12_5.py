class DataAnalyzer:
    def determine_range(self, data):
        if not data:
            return None
        minimum = data[0]
        maximum = data[0]
        for x in data:
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x
        return (minimum, maximum)
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10.5, 2.1, 99.0, 45.3, 12.8]
    sample_data2 = [5, -10, 0, 33, -50, 100]
    sample_data3 = []
    result1 = analyzer.determine_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    result2 = analyzer.determine_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")
    result3 = analyzer.determine_range(sample_data3)
    print(f"Data: {sample_data3}, Range: {result3}")