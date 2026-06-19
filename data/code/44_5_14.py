class RectangleUtils:
    @staticmethod
    def calculate_perimeter(length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Length and width must be numeric values.")
        return 2 * (length + width)

if __name__ == '__main__':
    sample_length = 10
    sample_width = 5
    try:
        perimeter = RectangleUtils.calculate_perimeter(sample_length, sample_width)
        print(f"Perimeter for length {sample_length} and width {sample_width}: {perimeter}")
    except TypeError as e:
        print(f"Error calculating perimeter: {e}")