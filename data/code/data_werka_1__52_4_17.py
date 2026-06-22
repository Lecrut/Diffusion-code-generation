class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    @staticmethod
    def calculate_area(base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        return 0.5 * base * height

if __name__ == '__main__':
    base_value = 10
    height_value = 5
    try:
        triangle = Triangle(base_value, height_value)
        area = Triangle.calculate_area(triangle.base, triangle.height)
        print(area)
    except ValueError as e:
        print(e)