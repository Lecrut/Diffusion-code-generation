class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    @property
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    sample_triangle = Triangle(5, 6, 7)
    print(sample_triangle.perimeter)