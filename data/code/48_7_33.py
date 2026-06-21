class Rectangle:
    MIN_DIMENSION = 0.0

    @staticmethod
    def validate_dimension(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Dimension must be a number.")
        if value <= Rectangle.MIN_DIMENSION:
            raise ValueError("Dimension must be greater than zero.")

    @staticmethod
    def calculate_area(base, height):
        Rectangle.validate_dimension(base)
        Rectangle.validate_dimension(height)
        return base * height

if __name__ == '__main__':
    sample_base = 8.1
    sample_height = 4.3
    area = Rectangle.calculate_area(sample_base, sample_height)
    print(area)