class RectangleUtils:
    @staticmethod
    def calculate_perimeter(dimensions):
        if len(dimensions) != 2:
            raise ValueError("Input list must contain exactly two dimensions (length and width).")
        length = dimensions[0]
        width = dimensions[1]
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
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