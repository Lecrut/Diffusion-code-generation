class Shape:
    @staticmethod
    def validate_dimensions(base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")

    @staticmethod
    def calculate_area(base, height):
        Shape.validate_dimensions(base, height)
        return 0.5 * base * height

if __name__ == '__main__':
    base = 12
    height = 3
    area = Shape.calculate_area(base, height)
    print(area)