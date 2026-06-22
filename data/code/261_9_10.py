class MedianCalculator:
    def find_median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n == 0:
            return None
        mid = n // 2
        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

if __name__ == '__main__':
    calculator = MedianCalculator()
    sample_data = [1, 3, 5, 7, 9]
    print(calculator.find_median(sample_data))
    sample_data_even = [1, 2, 3, 4]
    print(calculator.find_median(sample_data_even))