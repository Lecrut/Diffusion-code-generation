class SumCalculator:

    def __init__(self):
        self.total_sum = 0

    def calculate_sum(self, start, end):
        if start > end:
            raise ValueError('Start value must be less than or equal to end value')
        self.total_sum = end * (end + 1) // 2 - (start - 1) * start // 2
        return self.total_sum
if __name__ == '__main__':
    calculator = SumCalculator()
    sample_start = 1
    sample_end = 1000
    result = calculator.calculate_sum(sample_start, sample_end)
    print(result)