class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        if self.base <= 0 or self.height <= 0:
            raise ValueError("Base and height must be positive numbers")
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_base = 12
    triangle_height = 6
    triangle = Triangle(triangle_base, triangle_height)
    area_result = triangle.calculate_area()
    print(area_result)