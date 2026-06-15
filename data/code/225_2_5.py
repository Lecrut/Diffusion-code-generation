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
    sample_data = [3.14, 1.0, 9.8, 4.5, 6.2]
    minimum, maximum, range_val = finder.calculate_range(sample_data)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Range: {range_val}")
    sample_data_empty = []
    minimum_e, maximum_e, range_e = finder.calculate_range(sample_data_empty)
    print(f"Empty list result (Min, Max, Range): ({minimum_e}, {maximum_e}, {range_e})")