class Triangle:
    MIN_VALUE = 0

    @staticmethod
    def validate_positive(value):
        if value <= Triangle.MIN_VALUE:
            raise ValueError("Base and height must be positive numbers.")

    @classmethod
    def calculate_area(cls, base, height):
        cls.validate_positive(base)
        cls.validate_positive(height)
        return 0.5 * base * height

if __name__ == '__main__':
    try:
        triangle = Triangle()
        area = triangle.calculate_area(9, 4)
        print(area)
    except ValueError as e:
        print(e)

    try:
        invalid_triangle = Triangle()
        area = invalid_triangle.calculate_area(-1, 2)
        print(area)
    except ValueError as e:
        print(e)