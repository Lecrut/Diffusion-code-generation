class RectangleUtils:
    @staticmethod
    def calculate_perimeter(dimensions):
        if len(dimensions) != 2:
            raise ValueError("Input list must contain exactly two dimensions (length and width).")
        length, width = dimensions
        if not all(isinstance(x, (int, float)) for x in dimensions):
            raise TypeError("Dimensions must be numeric values.")
        perimeter = 2 * (length + width)
        return perimeter

if __name__ == '__main__':
    sample_dimensions_valid = [7.5, 3.2]
    try:
        perimeter1 = RectangleUtils.calculate_perimeter(sample_dimensions_valid)
        print(f"Perimeter for {sample_dimensions_valid}: {perimeter1}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_valid}: {e}")

    sample_dimensions_invalid_count = [7.5, 3.2, 1.0]
    try:
        perimeter2 = RectangleUtils.calculate_perimeter(sample_dimensions_invalid_count)
        print(f"Perimeter for {sample_dimensions_invalid_count}: {perimeter2}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_invalid_count}: {e}")

    sample_dimensions_invalid_type = [7.5, "three"]
    try:
        perimeter3 = RectangleUtils.calculate_perimeter(sample_dimensions_invalid_type)
        print(f"Perimeter for {sample_dimensions_invalid_type}: {perimeter3}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_invalid_type}: {e}")