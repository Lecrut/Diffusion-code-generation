class MedianCalculator:
    @staticmethod
    def calculate_median(data):
        n = len(data)
        if n == 0:
            raise ValueError("Input list cannot be empty")
        sorted_data = sorted(data)
        mid_index = n // 2
        if n % 2 == 1:
            return sorted_data[mid_index]
        else:
            return (sorted_data[mid_index - 1] + sorted_data[mid_index]) / 2

if __name__ == '__main__':
    sample_values = [10, 5, 8, 12, 3]
    calculator = MedianCalculator()
    print(calculator.calculate_median(sample_values))