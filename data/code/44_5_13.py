class RectangleUtils:
    @staticmethod
    def calculate_perimeter(dimensions):
        if len(dimensions) != 2:
            raise ValueError("Input list must contain exactly two dimensions (length and width).")
        length, width = dimensions
        if not all(isinstance(x, (int, float)) for x in dimensions):
            raise TypeError("Dimensions must be numeric values.")
        return 2 * (length + width)

if __name__ == '__main__':
    sample_dimensions_valid = [7, 3]
    sample_dimensions_invalid_count = [7, 3, 1]
    sample_dimensions_invalid_type = [7, "three"]
    
    try:
        perimeter_valid = RectangleUtils.calculate_perimeter(sample_dimensions_valid)
        print(f"Perimeter for {sample_dimensions_valid}: {perimeter_valid}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_valid}: {e}")

    try:
        perimeter_invalid_count = RectangleUtils.calculate_perimeter(sample_dimensions_invalid_count)
        print(f"Perimeter for {sample_dimensions_invalid_count}: {perimeter_invalid_count}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_invalid_count}: {e}")

    try:
        perimeter_invalid_type = RectangleUtils.calculate_perimeter(sample_dimensions_invalid_type)
        print(f"Perimeter for {sample_dimensions_invalid_type}: {perimeter_invalid_type}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter for {sample_dimensions_invalid_type}: {e}")