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
    sample_data1 = [10.5, 3.2, 9.8, 4.1, 7.6]
    sample_data2 = [5, 1, 8, 3, 10]
    sample_data3 = []
    min1, max1 = analyzer.determine_range(sample_data1)
    print(f"Data: {sample_data1}")
    print(f"Range (Min, Max): ({min1}, {max1})")
    min2, max2 = analyzer.determine_range(sample_data2)
    print(f"Data: {sample_data2}")
    print(f"Range (Min, Max): ({min2}, {max2})")
    min3, max3 = analyzer.determine_range(sample_data3)
    print(f"Data: {sample_data3}")
    print(f"Range (Min, Max): ({min3}, {max3})")