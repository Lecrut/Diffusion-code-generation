class Triangle:
    def __init__(self, base, height):
        if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
            raise ValueError("Base and height must be numbers.")
        if base <= 0 or height <= 0:
            raise ValueError("Base and height must be positive numbers.")
        self.base = base
        self.height = height

    def calculate_area(self):
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