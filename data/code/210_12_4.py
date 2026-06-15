class DataAnalyzer:
    def determine_range(self, data):
        if not data:
            return None
        minimum = data[0]
        maximum = data[0]
        for x in data[1:]:
            if x < minimum:
                minimum = x
            elif x > maximum:
                maximum = x
        return (minimum, maximum)
if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10.5, 3.2, 8.9, 1.1, 5.0]
    sample_data2 = [42, 15, 88, 3, 99]
    sample_data3 = []
    print(analyzer.determine_range(sample_data1))
    print(analyzer.determine_range(sample_data2))
    print(analyzer.determine_range(sample_data3))