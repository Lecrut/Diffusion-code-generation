class MinMaxFinder:
    def calculate_range(self, numbers):
        if not numbers:
            return None, None, None
        minimum = min(numbers)
        maximum = max(numbers)
        range_value = maximum - minimum
        return minimum, maximum, range_value
if __name__ == '__main__':
    finder = MinMaxFinder()
    sample_data = [3.14, 1.618, 2.718, 0.577, 4.0]
    minimum_val, maximum_val, difference = finder.calculate_range(sample_data)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")
    print(f"Range (Max - Min): {difference}")