class MedianCalculator:
    def __init__(self):
        self.data = []

    def add_value(self, value):
        self.data.append(value)
        self.data.sort()

    def get_median(self):
        n = len(self.data)
        if n == 0:
            return None
        elif n % 2 == 1:
            return self.data[n // 2]
        else:
            mid1 = self.data[n // 2 - 1]
            mid2 = self.data[n // 2]
            return (mid1 + mid2) / 2

if __name__ == '__main__':
    calculator = MedianCalculator()
    sample_values = [5, 2, 8, 1, 9, 3, 7, 4, 6]
    for value in sample_values:
        calculator.add_value(value)
    
    print("Median:", calculator.get_median())