class MedianCalculator:
    @staticmethod
    def calculate_median(data):
        n = len(data)
        if n == 0:
            return None
        sorted_data = sorted(data)
        mid = n // 2
        if n % 2 == 1:
            return sorted_data[mid]
        else:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0

if __name__ == '__main__':
    large_dataset = [random.randint(1, 1000000) for _ in range(1000000)]
    calculator = MedianCalculator()
    median_value = calculator.calculate_median(large_dataset)
    print(median_value)