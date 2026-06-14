class SampleAnalyzer:
    def __init__(self):
        pass
    def get_average(self, samples):
        if not samples:
            return 0
        return sum(samples) / len(samples)
if __name__ == '__main__':
    analyzer = SampleAnalyzer()
    data1 = [10, 20, 30, 40, 50]
    result1 = analyzer.get_average(data1)
    print(f"Average of {data1}: {result1}")
    data2 = [5, 15, 25]
    result2 = analyzer.get_average(data2)
    print(f"Average of {data2}: {result2}")
    data3 = []
    result3 = analyzer.get_average(data3)
    print(f"Average of {data3}: {result3}")