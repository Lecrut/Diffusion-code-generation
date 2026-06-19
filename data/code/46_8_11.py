class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not self._is_valid_triangle():
            raise ValueError("Invalid triangle sides")

    def _is_valid_triangle(self):
        return (self.sides[0] + self.sides[1] > self.sides[2] and
                self.sides[0] + self.sides[2] > self.sides[1] and
                self.sides[1] + self.sides[2] > self.sides[0])

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle = Triangle(5, 7, 9)
        print(triangle.perimeter())
    except ValueError as e:
        print(e)