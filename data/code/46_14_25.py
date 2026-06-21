class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3
        self._validate_sides()
    
    def _validate_sides(self):
        if not all(isinstance(side, (int, float)) and side > 0 for side in [self.side1, self.side2, self.side3]):
            raise ValueError("Side lengths must be positive numbers.")
    
    def perimeter(self):
        return self.side1 + self.side2 + self.side3

if __name__ == '__main__':
    triangle1 = Triangle(5, 6, 7)
    print(triangle1.perimeter())
    
    triangle2 = Triangle(3, 4, 5)
    print(triangle2.perimeter())
    
    triangle3 = Triangle(9, 10, 11)
    print(triangle3.perimeter())