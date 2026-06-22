class Triangle:
    def __init__(self, side_a, side_b, side_c):
        if all(side > 0 for side in (side_a, side_b, side_c)):
            self.side_a = side_a
            self.side_b = side_b
            self.side_c = side_c
        else:
            raise ValueError("All sides must be positive numbers")

    @property
    def perimeter(self):
        return self.side_a + self.side_b + self.side_c

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    print(triangle.perimeter)