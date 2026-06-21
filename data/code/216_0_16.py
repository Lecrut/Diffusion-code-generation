import statistics

class MedianCalculator:
    def calculate_median(self, data):
        return statistics.median(data)

if __name__ == '__main__':
    calculator = MedianCalculator()
    sample_list_odd = [1, 5, 3, 7, 9]
    sample_list_even = [10, 20, 30, 40]
    print(f"Median of {sample_list_odd}: {calculator.calculate_median(sample_list_odd)}")
    print(f"Median of {sample_list_even}: {calculator.calculate_median(sample_list_even)}")