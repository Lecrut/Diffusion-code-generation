class Rectangle:
    MIN_DIMENSION = 0

    @staticmethod
    def validate_dimension(dimension):
        if not isinstance(dimension, (int, float)) or dimension <= Rectangle.MIN_DIMENSION:
            raise ValueError("Dimension must be a positive number.")

    @staticmethod
    def calculate_perimeter(length, width):
        try:
            Rectangle.validate_dimension(length)
            Rectangle.validate_dimension(width)
            perimeter = 2 * (length + width)
            return perimeter
        except ValueError as e:
            return str(e)

if __name__ == '__main__':
    sample_length = 8.5
    sample_width = 3.2
    result = Rectangle.calculate_perimeter(sample_length, sample_width)
    print(result)