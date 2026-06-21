class GeometryHelper:
    @staticmethod
    def calculate_perimeter(length, width):
        if not isinstance(length, (int, float)) or not isinstance(width, (int, float)):
            raise TypeError("Length and width must be numeric values.")
        return 2 * (length + width)

if __name__ == '__main__':
    rectangle_length = 7
    rectangle_width = 4
    try:
        perimeter = GeometryHelper.calculate_perimeter(rectangle_length, rectangle_width)
        print(f"The perimeter of the rectangle with length {rectangle_length} and width {rectangle_width} is: {perimeter}")
    except (ValueError, TypeError) as e:
        print(f"Error calculating perimeter: {e}")