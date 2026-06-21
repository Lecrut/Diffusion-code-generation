class Rectangle:
    MIN_DIMENSION = 0.0

    @staticmethod
    def validate_dimensions(length, width):
        if length <= Rectangle.MIN_DIMENSION or width <= Rectangle.MIN_DIMENSION:
            raise ValueError("Length and width must be positive numbers.")

    @staticmethod
    def calculate_area(length, width):
        Rectangle.validate_dimensions(length, width)
        return length * width

if __name__ == '__main__':
    sample_length = 6.0
    sample_width = 4.0
    area_result = Rectangle.calculate_area(sample_length, sample_width)
    print(area_result)