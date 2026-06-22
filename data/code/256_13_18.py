class RangeCalculator:
    MIN_VAL = float('inf')
    MAX_VAL = float('-inf')

    @staticmethod
    def calculate_min_max(data):
        min_val, max_val = RangeCalculator.MIN_VAL, RangeCalculator.MAX_VAL
        for value in data:
            if value < min_val:
                min_val = value
            elif value > max_val:
                max_val = value
        return min_val, max_val

    def __init__(self, data):
        self.min_val, self.max_val = self.calculate_min_max(data)

    def calculate_range(self):
        return self.max_val - self.min_val

if __name__ == '__main__':
    sample_data = [10, 25, 35, 45, 60]
    calculator = RangeCalculator(sample_data)
    print(calculator.calculate_range())