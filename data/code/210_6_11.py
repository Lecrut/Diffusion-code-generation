class RangeCalculator:
    def __init__(self, data):
        self.data = iter(data)
    
    def compute_range(self):
        min_val = max_val = next(self.data)
        for value in self.data:
            if value < min_val:
                min_val = value
            elif value > max_val:
                max_val = value
        return max_val - min_val

if __name__ == '__main__':
    sample_data = (x**2 for x in range(1000000))
    calculator = RangeCalculator(sample_data)
    print(calculator.compute_range())