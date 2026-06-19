class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle1 = Triangle(10.0, 5.0)
    area1 = triangle1.calculate_area()
    print(f"Area of triangle with base 10.0 and height 5.0: {area1}")

    triangle2 = Triangle(7.5, 3.2)
    area2 = triangle2.calculate_area()
    print(f"Area of triangle with base 7.5 and height 3.2: {area2}")