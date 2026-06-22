class RangeCalculator:
    def __init__(self):
        self.min_val = float('inf')
        self.max_val = float('-inf')

    def update(self, value):
        if value < self.min_val:
            self.min_val = value
        elif value > self.max_val:
            self.max_val = value

    def calculate_range(self):
        return self.max_val - self.min_val

if __name__ == '__main__':
    calculator = RangeCalculator()
    sample_data = [10, 25, 35, 45, 60]
    for data in sample_data:
        calculator.update(data)
    print(calculator.calculate_range())