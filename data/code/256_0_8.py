class RangeCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_range(self):
        if not self.data:
            return 0.0
        minimum = min(self.data)
        maximum = max(self.data)
        return maximum - minimum

if __name__ == '__main__':
    calculator = RangeCalculator([10.5, 3.2, 8.8, 1.1, 5.0])
    range_value = calculator.calculate_range()
    print(range_value)