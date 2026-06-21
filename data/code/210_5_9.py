class RangeCalculator:
    def __init__(self, data):
        if not all(isinstance(item, (int, float)) for item in data):
            raise TypeError("Data must be a list of numbers")
        self.data = data

    def calculate_range(self):
        min_val = max_val = self.data[0]
        for item in self.data:
            if item < min_val:
                min_val = item
            elif item > max_val:
                max_val = item
        return min_val, max_val

if __name__ == '__main__':
    sample_data = [10, 20, 30, 40, 50]
    calculator_instance = RangeCalculator(sample_data)
    min_value, max_value = calculator_instance.calculate_range()
    print(f"Minimum value: {min_value}")
    print(f"Maximum value: {max_value}")