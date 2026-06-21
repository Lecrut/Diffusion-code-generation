def calculate_triangle_perimeter(side1, side2, side3):
    if not all(isinstance(x, (int, float)) and x > 0 for x in [side1, side2, side3]):
        raise ValueError("All sides must be positive numbers.")
    return sum([side1, side2, side3])

class Triangle:
    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def perimeter(self):
        return calculate_triangle_perimeter(self.side1, self.side2, self.side3)

if __name__ == '__main__':
    sample_side1 = 7.5
    sample_side2 = 9.2
    sample_side3 = 4.8
    triangle = Triangle(sample_side1, sample_side2, sample_side3)
    perimeter = triangle.perimeter()
    print(perimeter)