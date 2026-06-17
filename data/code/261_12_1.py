class SampleAnalyzer:
    def get_median(self, samples):
        sorted_samples = sorted(samples)
        n = len(sorted_samples)
        if n == 0:
            return None
        elif n % 2 == 1:
            return sorted_samples[n // 2]
        else:
            mid1 = sorted_samples[n // 2 - 1]
            mid2 = sorted_samples[n // 2]
            return (mid1 + mid2) / 2
if __name__ == '__main__':
    analyzer = SampleAnalyzer()
    sample1 = [1, 3, 5, 7, 9]
    sample2 = [4, 1, 8, 2, 6]
    sample3 = [10, 20, 30, 40]
    sample4 = []
    median1 = analyzer.get_median(sample1)
    print(f"Median of {sample1}: {median1}")
    median2 = analyzer.get_median(sample2)
    print(f"Median of {sample2}: {median2}")
    median3 = analyzer.get_median(sample3)
    print(f"Median of {sample3}: {median3}")
    median4 = analyzer.get_median(sample4)
    print(f"Median of {sample4}: {median4}")