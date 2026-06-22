import random

class MedianCalculator:
    def __init__(self, data):
        self.data = data
    
    def calculate_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2.0
        else:
            return sorted_data[mid]

if __name__ == '__main__':
    sample_data = [random.randint(1, 1000) for _ in range(100)]
    calculator = MedianCalculator(sample_data)
    median_value = calculator.calculate_median()
    print(median_value)