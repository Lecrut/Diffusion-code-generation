class ValueExtremes:
    def __init__(self):
        self.values = []

    def add_value(self, value):
        self.values.append(value)

    def find_min(self):
        if not self.values:
            return None
        return min(self.values)

    def find_max(self):
        if not self.values:
            return None
        return max(self.values)

if __name__ == '__main__':
    extremes = ValueExtremes()
    sample_values = [10, 5, 20, 8, 15]
    for value in sample_values:
        extremes.add_value(value)
    
    min_val = extremes.find_min()
    max_val = extremes.find_max()
    
    print(f"Minimum value: {min_val}")
    print(f"Maximum value: {max_val}")