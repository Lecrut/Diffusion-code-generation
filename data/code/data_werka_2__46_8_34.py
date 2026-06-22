def calculate_triangle_perimeter(side1, side2, side3):
    return sum([side1, side2, side3])

class Triangle:
    def __init__(self, side1, side2, side3):
        self.sides = [side1, side2, side3]
    
    def perimeter(self):
        return calculate_triangle_perimeter(*self.sides)
    
    def is_valid(self):
        a, b, c = sorted(self.sides)
        return a + b > c

if __name__ == '__main__':
    sample_side1 = 7
    sample_side2 = 10
    sample_side3 = 5
    triangle = Triangle(sample_side1, sample_side2, sample_side3)
    
    perimeter = triangle.perimeter()
    print(f"Perimeter: {perimeter}")
    
    is_valid = triangle.is_valid()
    print(f"Is valid triangle: {is_valid}")