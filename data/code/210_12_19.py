class DataAnalyzer:
    @staticmethod
    def determine_range(data):
        if not data:
            return None, None
        minimum = maximum = data[0]
        for x in data[1:]:
            if x < minimum:
                minimum = x
            elif x > maximum:
                maximum = x
        return minimum, maximum

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    sample_data1 = [10.5, 3.2, 8.9, 1.1, 5.0]
    result1 = analyzer.determine_range(sample_data1)
    print(f"Data: {sample_data1}, Range: {result1}")