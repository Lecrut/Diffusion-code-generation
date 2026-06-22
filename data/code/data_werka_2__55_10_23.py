class Triangle:

    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]

    @property
    def perimeter(self):
        return sum(self.sides)
if __name__ == '__main__':
    triangle1 = Triangle(3, 4, 5)
    print(triangle1.perimeter)
    triangle2 = Triangle(6, 8, 10)
    print(triangle2.perimeter)
    triangle3 = Triangle(7, 9, 12)
    print(triangle3.perimeter)