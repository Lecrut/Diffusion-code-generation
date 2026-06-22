class MedianCalculator:
    def __init__(self, numbers):
        self.numbers = sorted(numbers)

    def calculate_median(self):
        n = len(self.numbers)
        mid = n // 2
        if n % 2 == 0:
            return (self.numbers[mid - 1] + self.numbers[mid]) / 2.0
        else:
            return float(self.numbers[mid])

if __name__ == '__main__':
    calculator = MedianCalculator([3.5, 1.2, 4.8, 2.9, 5.1])
    print(calculator.calculate_median())