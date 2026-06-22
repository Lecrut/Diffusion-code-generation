class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.validate_dimensions()

    def validate_dimensions(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers.")

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    base_value = 6
    height_value = 8
    triangle_instance = Triangle(base_value, height_value)
    area_result = triangle_instance.calculate_area()
    print(area_result)