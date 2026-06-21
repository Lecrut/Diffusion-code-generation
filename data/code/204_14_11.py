class MedianCalculator:
    def __init__(self, data):
        self.data = sorted(data)

    def find_median(self):
        n = len(self.data)
        if n == 0:
            return None
        else:
            middle_index = n // 2
            if n % 2 == 1:
                return self.data[middle_index]
            else:
                return (self.data[middle_index - 1] + self.data[middle_index]) / 2

if __name__ == '__main__':
    calculator = MedianCalculator([5.5, 6.6, 7.7])
    print(f"Median: {calculator.find_median()}")

    calculator = MedianCalculator([100])
    print(f"Median: {calculator.find_median()}")

    calculator = MedianCalculator([])
    print(f"Median: {calculator.find_median()}")