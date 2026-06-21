import statistics

class MedianCalculator:
    def __init__(self, data):
        self.data = sorted(data)
    
    def calculate_median(self):
        return statistics.median(self.data)

if __name__ == '__main__':
    calculator_odd = MedianCalculator([1, 5, 3, 7, 9])
    calculator_even = MedianCalculator([10, 20, 30, 40])
    print(f"Median of odd list: {calculator_odd.calculate_median()}")
    print(f"Median of even list: {calculator_even.calculate_median()}")