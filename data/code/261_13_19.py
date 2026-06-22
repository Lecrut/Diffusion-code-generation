import random

class MedianCalculator:
    def __init__(self):
        self.data = []

    def add_value(self, value):
        self.data.append(value)

    def calculate_median(self):
        sorted_data = sorted(self.data)
        n = len(sorted_data)
        mid = n // 2
        if n % 2 == 0:
            return (sorted_data[mid - 1] + sorted_data[mid]) / 2
        else:
            return sorted_data[mid]

if __name__ == '__main__':
    calculator = MedianCalculator()
    for _ in range(100):
        calculator.add_value(random.randint(1, 1000))
    median_value = calculator.calculate_median()
    print(median_value)