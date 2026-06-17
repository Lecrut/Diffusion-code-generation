class SampleAnalyzer:
    def get_median(self, samples):
        sorted_samples = sorted(samples)
        n = len(sorted_samples)
        if n == 0:
            return None
        elif n % 2 == 1:
            median = sorted_samples[n // 2]
        else:
            mid1 = sorted_samples[n // 2 - 1]
            mid2 = sorted_samples[n // 2]
            median = (mid1 + mid2) / 2.0
        return median
if __name__ == '__main__':
    analyzer = SampleAnalyzer()
    sample1 = [1, 3, 5, 7, 9]
    sample2 = [2, 4, 6, 8, 10]
    sample3 = [1, 2, 3, 4]
    sample4 = [1, 2, 3, 4, 5, 6]
    sample5 = [10, 20, 30]
    sample6 = []
    print(f"Median of {sample1}: {analyzer.get_median(sample1)}")
    print(f"Median of {sample2}: {analyzer.get_median(sample2)}")
    print(f"Median of {sample3}: {analyzer.get_median(sample3)}")
    print(f"Median of {sample4}: {analyzer.get_median(sample4)}")
    print(f"Median of {sample5}: {analyzer.get_median(sample5)}")
    print(f"Median of {sample6}: {analyzer.get_median(sample6)}")