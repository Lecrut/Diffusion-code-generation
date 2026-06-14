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
    minimum_val, maximum_val, difference = finder.calculate_range(sample_data)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")
    print(f"Range (Max - Min): {difference}")
    sample_data_2 = [-10.5, 0.0, 5.2, -3.14]
    minimum_val_2, maximum_val_2, difference_2 = finder.calculate_range(sample_data_2)
    print(f"Minimum: {minimum_val_2}")
    print(f"Maximum: {maximum_val_2}")
    print(f"Range (Max - Min): {difference_2}")
    empty_data = []
    min_val_3, max_val_3, diff_3 = finder.calculate_range(empty_data)
    print(f"Empty list result: Minimum={min_val_3}, Maximum={max_val_3}, Range={diff_3}")