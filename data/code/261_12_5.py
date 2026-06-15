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
    sample1 = [1, 3, 2]
    sample2 = [5, 2, 8, 1, 9]
    sample3 = [10, 20, 30, 40]
    sample4 = []
    print(f"Median of {sample1}: {analyzer.get_median(sample1)}")
    print(f"Median of {sample2}: {analyzer.get_median(sample2)}")
    print(f"Median of {sample3}: {analyzer.get_median(sample3)}")
    print(f"Median of {sample4}: {analyzer.get_median(sample4)}")