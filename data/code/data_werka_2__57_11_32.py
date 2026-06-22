class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def validate_dimensions(self):
        if self.base <= 0:
            raise ValueError("Base must be a positive number.")
        if self.height <= 0:
            raise ValueError("Height must be a positive number.")

    def calculate_area(self):
        self.validate_dimensions()
        return 0.5 * self.base * self.height

def main():
    try:
        triangle = Triangle(6, 8)
        area = triangle.calculate_area()
        print(area)
    except ValueError as e:
        print(e)

if __name__ == '__main__':
    main()