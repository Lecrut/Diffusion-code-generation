class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle_base = 7.0
    triangle_height = 4.0
    my_triangle = Triangle(triangle_base, triangle_height)
    calculated_area = my_triangle.area()
    print(calculated_area)