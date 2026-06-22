class MedianCalculator:
    def __init__(self, samples):
        self.samples = samples

    def calculate_median(self):
        sorted_samples = sorted(self.samples)
        n = len(sorted_samples)
        if n % 2 == 1:
            return sorted_samples[n // 2]
        else:
            mid1 = sorted_samples[n // 2 - 1]
            mid2 = sorted_samples[n // 2]
            return (mid1 + mid2) / 2

if __name__ == '__main__':
    calculator = MedianCalculator([10, 5, 8, 12, 3])
    print(calculator.calculate_median())