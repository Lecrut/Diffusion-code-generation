class Triangle:
    def __init__(self, side1, side2, side3):
        if all(side > 0 for side in (side1, side2, side3)):
            self.sides = [side1, side2, side3]
        else:
            raise ValueError("All sides must be positive numbers")

    @property
    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    valid_triangle = Triangle(3, 4, 5)
    print(valid_triangle.perimeter)

    try:
        invalid_triangle = Triangle(-1, 4, 5)
    except ValueError as e:
        print(e)