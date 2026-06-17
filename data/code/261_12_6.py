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
    sample_data_1 = [1, 3, 5, 7, 9]
    sample_data_2 = [1, 2, 3, 4, 5, 6]
    sample_data_3 = [10, 20, 30, 40]
    sample_data_4 = [1, 2, 3, 4]
    median_1 = analyzer.get_median(sample_data_1)
    print(f"Median of {sample_data_1}: {median_1}")
    median_2 = analyzer.get_median(sample_data_2)
    print(f"Median of {sample_data_2}: {median_2}")
    median_3 = analyzer.get_median(sample_data_3)
    print(f"Median of {sample_data_3}: {median_3}")
    median_4 = analyzer.get_median(sample_data_4)
    print(f"Median of {sample_data_4}: {median_4}")