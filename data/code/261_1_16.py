class MedianCalculator:
    @staticmethod
    def calculate_median(data):
        n = len(data)
        sorted_data = sorted(data)
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2

if __name__ == '__main__':
    sample_data1 = [5, 2, 8, 1, 9]
    print(f"Data: {sample_data1}, Median: {MedianCalculator.calculate_median(sample_data1)}")
    sample_data2 = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
    print(f"Data: {sample_data2}, Median: {MedianCalculator.calculate_median(sample_data2)}")
    sample_data3 = [10, 20, 30, 40]
    print(f"Data: {sample_data3}, Median: {MedianCalculator.calculate_median(sample_data3)}")