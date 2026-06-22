class MedianCalculator:
    @staticmethod
    def calculate_median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n == 0:
            return None
        mid_index = n // 2
        if n % 2 == 1:
            median = sorted_data[mid_index]
        else:
            median = (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2
        return median

if __name__ == '__main__':
    calculator = MedianCalculator()
    samples = [
        [1, 5, 2, 8],
        [10, 20, 30, 40, 50],
        [7, 1, 4, 9, 2]
    ]
    for sample in samples:
        median_value = calculator.calculate_median(sample)
        print(median_value)