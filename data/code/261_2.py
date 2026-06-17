class StatisticsCalculator:
    def get_median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n == 0:
            return None
        elif n % 2 == 1:
            median = sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            median = (mid1 + mid2) / 2.0
        return median
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    sample_data1 = [1, 3, 5, 7, 9]
    sample_data2 = [4, 1, 8, 3, 6]
    sample_data3 = [10, 20, 30, 40]
    sample_data4 = []
    median1 = calculator.get_median(sample_data1)
    print(f"Median of {sample_data1}: {median1}")
    median2 = calculator.get_median(sample_data2)
    print(f"Median of {sample_data2}: {median2}")
    median3 = calculator.get_median(sample_data3)
    print(f"Median of {sample_data3}: {median3}")
    median4 = calculator.get_median(sample_data4)
    print(f"Median of {sample_data4}: {median4}")