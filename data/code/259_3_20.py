class PrecisionAnalyzer:
    def __init__(self, values):
        if not values:
            raise ValueError("Input list cannot be empty")
        self.values = values

    def find_min(self):
        min_val = float('inf')
        for value in self.values:
            if value < min_val:
                min_val = value
        return min_val

    def find_max(self):
        max_val = float('-inf')
        for value in self.values:
            if value > max_val:
                max_val = value
        return max_val

if __name__ == '__main__':
    sample_values = [3.141592653589793, 2.718281828459045, 1.618033988749895, 0.5772156649015328]
    analyzer = PrecisionAnalyzer(sample_values)
    min_val = analyzer.find_min()
    max_val = analyzer.find_max()
    print(f"Minimum: {min_val}, Maximum: {max_val}")