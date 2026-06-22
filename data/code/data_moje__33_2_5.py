class Triangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive values")
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    base_val = 10
    height_val = 5
    triangle = Triangle(base_val, height_val)
    area = triangle.calculate_area()
    print(area)