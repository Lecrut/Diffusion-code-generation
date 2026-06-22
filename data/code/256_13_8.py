class RangeCalculator:
    MIN_VALUE = float('inf')
    MAX_VALUE = float('-inf')

    def __init__(self):
        self.min_val = self.MIN_VALUE
        self.max_val = self.MAX_VALUE

    @staticmethod
    def update(current_min, current_max, value):
        if value < current_min:
            return value, current_max
        elif value > current_max:
            return current_min, value
        else:
            return current_min, current_max

    def calculate_range(self):
        return self.max_val - self.min_val

if __name__ == '__main__':
    calculator = RangeCalculator()
    sample_data = [10, 25, 35, 45, 60]
    for data in sample_data:
        calculator.min_val, calculator.max_val = RangeCalculator.update(calculator.min_val, calculator.max_val, data)
    print(calculator.calculate_range())