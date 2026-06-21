class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self._validate_sides()
    
    def _validate_sides(self):
        if not all(side > 0 for side in (self.side1, self.side2, self.side3)):
            raise ValueError("Side lengths must be positive numbers.")
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    print(triangle.perimeter())
    triangle = Triangle(6, 7, 8)
    print(triangle.perimeter())