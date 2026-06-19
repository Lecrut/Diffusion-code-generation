import math

class Triangle:

    def __init__(self, side1, side2=None):
        self.side1 = side1
        self.side2 = side2 if side2 else side1

    def area(self):
        if self.side2 == self.side1:
            return math.sqrt(3) / 4 * self.side1 ** 2
        else:
            height = math.sqrt(self.side2 ** 2 - (self.side1 / 2) ** 2)
            return 0.5 * self.side1 * height

def calculate_area_ratio(side1_eq, side1_iso, side2_iso):
    equilateral_triangle = Triangle(side1_eq)
    isosceles_triangle = Triangle(side1_iso, side2_iso)
    area_eq = equilateral_triangle.area()
    area_iso = isosceles_triangle.area()
    return area_eq / area_iso
if __name__ == '__main__':
    side_length_eq = 6.0
    base_side_iso = 8.0
    equal_sides_iso = 5.0
    ratio = calculate_area_ratio(side_length_eq, base_side_iso, equal_sides_iso)
    print(ratio)