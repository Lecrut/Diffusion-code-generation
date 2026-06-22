class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
        if not all(isinstance(side, int) and side > 0 for side in self.sides):
            raise ValueError("Side lengths must be positive integers")
        if not (self._is_valid_triangle()):
            raise ValueError("Invalid triangle sides")

    def _is_valid_triangle(self):
        a, b, c = sorted(self.sides)
        return a + b > c

    def perimeter(self):
        return sum(self.sides)

if __name__ == '__main__':
    try:
        triangle1 = Triangle(3, 4, 5)
        print(triangle1.perimeter())
        
        triangle2 = Triangle(7, 10, 5)
        print(triangle2.perimeter())
    except ValueError as e:
        print(e)