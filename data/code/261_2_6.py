class StatisticsCalculator:
    def get_median(self, data):
        sorted_data = sorted(data)
        n = len(sorted_data)
        if n == 0:
            return None
        elif n % 2 == 1:
            return sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2
if __name__ == '__main__':
    calculator = StatisticsCalculator()
    data1 = [1, 3, 5, 7, 9]
    median1 = calculator.get_median(data1)
    print(f"Data: {data1}, Median: {median1}")
    data2 = [4, 1, 8, 3, 6, 2]
    median2 = calculator.get_median(data2)
    print(f"Data: {data2}, Median: {median2}")
    data3 = [10, 20, 30, 40]
    median3 = calculator.get_median(data3)
    print(f"Data: {data3}, Median: {median3}")
    data4 = [5]
    median4 = calculator.get_median(data4)
    print(f"Data: {data4}, Median: {median4}")
    data5 = []
    median5 = calculator.get_median(data5)
    print(f"Data: {data5}, Median: {median5}")