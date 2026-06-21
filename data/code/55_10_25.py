class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    @property
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle_types = {
        'right_angled': [3, 4, 5],
        'acute_scalene': [7, 10, 5],
        'obtuse_isosceles': [6, 8, 10]
    }
    triangle = Triangle(*triangle_types['right_angled'])
    print(triangle.perimeter)