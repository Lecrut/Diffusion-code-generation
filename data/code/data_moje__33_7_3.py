class Triangle:
    def __init__(self, base, height):
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers")
        self.base = float(base)
        self.height = float(height)

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    sample_base = 7.25
    sample_height = 3.14
    try:
        triangle = Triangle(sample_base, sample_height)
        print(triangle.calculate_area())
    except ValueError as e:
        print(e)