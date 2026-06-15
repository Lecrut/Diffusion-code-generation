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
    minimum_val, maximum_val, difference = finder.calculate_range(sample_data)
    print(f"Minimum: {minimum_val}")
    print(f"Maximum: {maximum_val}")
    print(f"Range (Max - Min): {difference}")
    sample_data_2 = [-5.5, 10.2, 0.0, -1.3]
    minimum_val_2, maximum_val_2, difference_2 = finder.calculate_range(sample_data_2)
    print(f"Minimum: {minimum_val_2}")
    print(f"Maximum: {maximum_val_2}")
    print(f"Range (Max - Min): {difference_2}")
    sample_data_3 = []
    minimum_val_3, maximum_val_3, difference_3 = finder.calculate_range(sample_data_3)
    print(f"Minimum: {minimum_val_3}")
    print(f"Maximum: {maximum_val_3}")
    print(f"Range (Max - Min): {difference_3}")