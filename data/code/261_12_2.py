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
            median = (mid1 + mid2) / 2
        return median
if __name__ == '__main__':
    analyzer = SampleAnalyzer()
    sample_data1 = [1, 3, 5, 7, 9]
    sample_data2 = [1, 2, 3, 4, 5, 6]
    sample_data3 = [10, 20, 30]
    sample_data4 = []
    median1 = analyzer.get_median(sample_data1)
    print(f"Median of {sample_data1}: {median1}")
    median2 = analyzer.get_median(sample_data2)
    print(f"Median of {sample_data2}: {median2}")
    median3 = analyzer.get_median(sample_data3)
    print(f"Median of {sample_data3}: {median3}")
    median4 = analyzer.get_median(sample_data4)
    print(f"Median of {sample_data4}: {median4}")