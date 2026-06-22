class MedianCalculator:
    def __init__(self, data):
        self.data = sorted(data)

    def calculate_median(self):
        n = len(self.data)
        if n % 2 == 1:
            return self.data[n // 2]
        else:
            mid1 = self.data[n // 2 - 1]
            mid2 = self.data[n // 2]
            return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_values = [10, 5, 8, 12, 3, 9, 6]
    calculator = MedianCalculator(sample_values)
    print(calculator.calculate_median())