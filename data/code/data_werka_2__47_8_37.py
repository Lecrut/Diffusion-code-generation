class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    base_length = 15
    height_length = 4
    triangle = Triangle(base_length, height_length)
    calculated_area = triangle.area()
    print(f"The area of the triangle is: {calculated_area}")