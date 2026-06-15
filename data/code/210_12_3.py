class DataAnalyzer:
    def determine_range(self, data):
        if not data:
            return None, None
        minimum = data[0]
        maximum = data[0]
        for x in data[1:]:
            if x < minimum:
                minimum = x
            elif x > maximum:
                maximum = x
        return minimum, maximum
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10, 5, 20, 15, 8]
    result1 = analyzer.determine_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")
    sample_data2 = [3.14, 1.618, 2.718, 0.577]
    result2 = analyzer.determine_range(sample_data2)
    print(f"Data: {sample_data2}, Range: {result2}")
    sample_data3 = [42]
    result3 = analyzer.determine_range(sample_data3)
    print(f"Data: {sample_data3}, Range: {result3}")
    sample_data4 = []
    result4 = analyzer.determine_range(sample_data4)
    print(f"Data: {sample_data4}, Range: {result4}")