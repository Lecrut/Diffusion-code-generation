class MedianCalculator:
    def __init__(self, data):
        self.data = sorted(data)
    
    def calculate_median(self):
        n = len(self.data)
        mid = n // 2
        if n % 2 == 0:
            return (self.data[mid - 1] + self.data[mid]) / 2
        else:
            return self.data[mid]

if __name__ == '__main__':
    calculator = MedianCalculator([10, 20, 30, 40, 50])
    print(f"Median of the list: {calculator.calculate_median()}")