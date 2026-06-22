class GeometryUtils:
    @staticmethod
    def calculate_triangle_area(base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        return 0.5 * base * height

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def get_area(self):
        return GeometryUtils.calculate_triangle_area(self.base, self.height)
    
    def describe(self):
        return f"Triangle with base {self.base} and height {self.height}"

if __name__ == '__main__':
    triangle = Triangle(6, 8)
    area = triangle.get_area()
    description = triangle.describe()
    print(area)
    print(description)