class DataAnalyzer:
    def determine_range(self, data):
        if not data:
            return None, None
        minimum = data[0]
        maximum = data[0]
        for x in data[1:]:
            if x < minimum:
                minimum = x
            if x > maximum:
                maximum = x
        return minimum, maximum
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10.5, 3.2, 8.9, 1.1, 5.0]
    sample_data2 = [42, 15, 88, 3, 99]
    sample_data3 = []
    sample_data4 = [7]
    min1, max1 = analyzer.determine_range(sample_data1)
    print(f"Data: {sample_data1}, Min: {min1}, Max: {max1}")
    min2, max2 = analyzer.determine_range(sample_data2)
    print(f"Data: {sample_data2}, Min: {min2}, Max: {max2}")
    min3, max3 = analyzer.determine_range(sample_data3)
    print(f"Data: {sample_data3}, Min: {min3}, Max: {max3}")
    min4, max4 = analyzer.determine_range(sample_data4)
    print(f"Data: {sample_data4}, Min: {min4}, Max: {max4}")