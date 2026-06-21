class FloatSumCalculator:
    def __init__(self, float_list):
        self.float_list = float_list

    def sum_positive_values(self):
        total = 0
        for num in self.float_list:
            if num > 0:
                total += num
        return total

if __name__ == '__main__':
    sample_values = [1.5, -2.3, 4.8, 0.0, -1.1, 3.2]
    calculator = FloatSumCalculator(sample_values)
    result = calculator.sum_positive_values()
    print(result)