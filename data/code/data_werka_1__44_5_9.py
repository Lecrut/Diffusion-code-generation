class RectangleUtils:
    @staticmethod
    def calculate_perimeter(dimensions):
        if len(dimensions) != 2:
            raise ValueError("Input list must contain exactly two dimensions (length and width).")
        length, width = dimensions
        if not all(isinstance(x, (int, float)) for x in [length, width]):
            raise TypeError("Dimensions must be numeric values.")
        return 2 * (length + width)

if __name__ == '__main__':
    sample_dimensions_valid = [10, 5]
    sample_dimensions_invalid_count = [10, 5, 2]
    sample_dimensions_invalid_type = [10, "five"]

    try:
        perimeter1 = RectangleUtils.calculate_perimeter(sample_dimensions_valid)
        print(f"Perimeter for {sample_dimensions_valid}: {perimeter1}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_valid}: {e}")

    try:
        perimeter2 = RectangleUtils.calculate_perimeter(sample_dimensions_invalid_count)
        print(f"Perimeter for {sample_dimensions_invalid_count}: {perimeter2}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_invalid_count}: {e}")

    try:
        perimeter3 = RectangleUtils.calculate_perimeter(sample_dimensions_invalid_type)
        print(f"Perimeter for {sample_dimensions_invalid_type}: {perimeter3}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_invalid_type}: {e}")