class Rectangle:
    MIN_DIMENSION = 0.0

    @staticmethod
    def validate_dimension(value, name):
        if not isinstance(value, (int, float)):
            raise TypeError(f"{name} must be a number.")
        if value <= Rectangle.MIN_DIMENSION:
            raise ValueError(f"{name} must be a positive number.")

    @staticmethod
    def calculate_area(base, height):
        Rectangle.validate_dimension(base, "Base")
        Rectangle.validate_dimension(height, "Height")
        return base * height

if __name__ == '__main__':
    base = 8.1
    height = 5.9
    area = Rectangle.calculate_area(base, height)
    print(area)