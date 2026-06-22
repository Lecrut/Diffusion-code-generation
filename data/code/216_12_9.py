class MedianCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_median(self):
        n = len(self.numbers)
        if n % 2 == 1:
            return self.numbers[n // 2]
        else:
            middle_index_1 = n // 2 - 1
            middle_index_2 = n // 2
            return (self.numbers[middle_index_1] + self.numbers[middle_index_2]) / 2

if __name__ == '__main__':
    calculator = MedianCalculator([10, 20, 30, 40, 50])
    median_value = calculator.calculate_median()
    print(median_value)