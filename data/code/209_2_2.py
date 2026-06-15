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
    data2 = [5.5, 6.5, 7.5]
    data3 = []
    avg1 = analyzer.get_average(data1)
    print(f"Average of {data1}: {avg1}")
    avg2 = analyzer.get_average(data2)
    print(f"Average of {data2}: {avg2}")
    avg3 = analyzer.get_average(data3)
    print(f"Average of {data3}: {avg3}")