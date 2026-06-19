class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
    
    def perimeter(self):
        return sum(self.sides)
    
    def is_valid(self):
        a, b, c = sorted(self.sides)
        return a + b > c

if __name__ == '__main__':
    triangle = Triangle(3, 4, 5)
    print("Perimeter:", triangle.perimeter())
    print("Is valid triangle:", triangle.is_valid())

    invalid_triangle = Triangle(1, 2, 3)
    print("Invalid triangle perimeter:", invalid_triangle.perimeter())
    print("Is invalid triangle valid:", invalid_triangle.is_valid())