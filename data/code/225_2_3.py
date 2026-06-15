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
    sample_data = [3.14, 1.0, 9.8, 5.5, 2.718]
    minimum, maximum, range_val = finder.calculate_range(sample_data)
    print(f"Minimum: {minimum}")
    print(f"Maximum: {maximum}")
    print(f"Range (Max - Min): {range_val}")
    sample_data_2 = [-10.5, 0.0, 5.2, -3.8]
    minimum_2, maximum_2, range_val_2 = finder.calculate_range(sample_data_2)
    print(f"Minimum: {minimum_2}")
    print(f"Maximum: {maximum_2}")
    print(f"Range (Max - Min): {range_val_2}")
    sample_data_3 = []
    minimum_3, maximum_3, range_val_3 = finder.calculate_range(sample_data_3)
    print(f"Minimum: {minimum_3}")
    print(f"Maximum: {maximum_3}")
    print(f"Range (Max - Min): {range_val_3}")