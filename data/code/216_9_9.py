class MedianCalculator:

    def __init__(self, data):
        self.data = sorted(data)

    def calculate_middle(self):
        n = len(self.data)
        middle_index = n // 2
        if n % 2 == 0:
            return (self.data[middle_index - 1] + self.data[middle_index]) / 2
        else:
            return self.data[middle_index]
if __name__ == '__main__':
    calculator = MedianCalculator([3, 1, 4, 1, 5, 9, 2])
    print(calculator.calculate_middle())
    calculator_odd = MedianCalculator([1, 3, 5, 7, 9])
    print(calculator_odd.calculate_middle())
    calculator_even = MedianCalculator([2, 4, 6, 8])
    print(calculator_even.calculate_middle())