class Triangle:

    def __init__(self, side_a, side_b, side_c):
        self.side_a = side_a
        self.side_b = side_b
        self.side_c = side_c

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c
if __name__ == '__main__':
    triangle_sides = (6, 8, 10)
    triangle = Triangle(*triangle_sides)
    print(triangle.perimeter)