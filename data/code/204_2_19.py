class MedianCalculator:
    DATA = [10, 20, 30, 40, 50]

    @staticmethod
    def calculate_median(data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

if __name__ == '__main__':
    calculator = MedianCalculator()
    median_value = calculator.calculate_median(MedianCalculator.DATA)
    print(median_value)