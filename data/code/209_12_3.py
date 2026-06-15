class SampleAnalyzer:
    def get_average(self, data_list):
        if not data_list:
            return 0
        return sum(data_list) / len(data_list)
if __name__ == '__main__':
    analyzer = SampleAnalyzer()
    sample1 = [10, 20, 30, 40, 50]
    sample2 = [5.5, 6.5, 7.5]
    sample3 = []
    average1 = analyzer.get_average(sample1)
    print(f"Average of sample1: {average1}")
    average2 = analyzer.get_average(sample2)
    print(f"Average of sample2: {average2}")
    average3 = analyzer.get_average(sample3)
    print(f"Average of sample3: {average3}")