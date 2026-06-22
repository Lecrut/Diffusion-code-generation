class MedianCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_median(self):
        n = len(self.data)
        if n == 0:
            return None
        sorted_data = sorted(self.data)
        middle_index = n // 2
        if n % 2 == 1:
            return sorted_data[middle_index]
        else:
            upper_middle_index = middle_index
            lower_middle_index = upper_middle_index - 1
            median = (sorted_data[lower_middle_index] + sorted_data[upper_middle_index]) / 2
            return median

if __name__ == '__main__':
    calculator = MedianCalculator([4, 7, 2, 5, 8])
    print(calculator.calculate_median())