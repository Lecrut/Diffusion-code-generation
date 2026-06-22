class MedianCalculator:

    @staticmethod
    def sort_data(data):
        return sorted(data)

    @staticmethod
    def calculate_median(sorted_data):
        n = len(sorted_data)
        if n % 2 == 1:
            return sorted_data[n // 2]
        else:
            mid1 = sorted_data[n // 2 - 1]
            mid2 = sorted_data[n // 2]
            return (mid1 + mid2) / 2.0

    @staticmethod
    def calculate(data):
        sorted_data = MedianCalculator.sort_data(data)
        return MedianCalculator.calculate_median(sorted_data)
if __name__ == '__main__':
    calculator = MedianCalculator()
    list1 = [5, 2, 8, 1, 9]
    median1 = calculator.calculate(list1)
    print(median1)