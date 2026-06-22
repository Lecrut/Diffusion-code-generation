class PrecisionCalculator:
    def __init__(self, values):
        self.values = values

    def find_min_max(self):
        if not self.values:
            return None, None
        min_val = max_val = self.values[0]
        for value in self.values[1:]:
            if value < min_val:
                min_val = value
            elif value > max_val:
                max_val = value
        return min_val, max_val

if __name__ == '__main__':
    sample_values = [3.141592653589793, 2.718281828459045, 1.618033988749895, 0.5772156649015328]
    calculator = PrecisionCalculator(sample_values)
    min_val, max_val = calculator.find_min_max()
    print(f"Minimum: {min_val}, Maximum: {max_val}")