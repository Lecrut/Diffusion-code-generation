class MedianCalculator:
    @staticmethod
    def find_median(sample):
        n = len(sample)
        if n == 0:
            return None
        sorted_sample = sorted(sample)
        mid = n // 2
        if n % 2 == 1:
            return sorted_sample[mid]
        else:
            return (sorted_sample[mid - 1] + sorted_sample[mid]) / 2.0

if __name__ == '__main__':
    calculator = MedianCalculator()
    sample_data = [
        [1, 3, 5],
        [7, 8, 9, 10],
        [],
        [4]
    ]
    for data in sample_data:
        print(calculator.find_median(data))