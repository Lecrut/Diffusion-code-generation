import statistics

class MedianCalculator:
    def __init__(self, data):
        self.data = data
    
    def calculate_median(self):
        return statistics.median(self.data)

if __name__ == '__main__':
    calculator1 = MedianCalculator([1, 3, 2])
    print(f"Median of [1, 3, 2]: {calculator1.calculate_median()}")
    
    calculator2 = MedianCalculator([1, 5, 3, 4, 2])
    print(f"Median of [1, 5, 3, 4, 2]: {calculator2.calculate_median()}")
    
    calculator3 = MedianCalculator([10, 20, 30, 40])
    print(f"Median of [10, 20, 30, 40]: {calculator3.calculate_median()}")