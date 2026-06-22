import math

class Triangle:

    def __init__(self, side1, side2, side3):
        self.side1 = side1
        self.side2 = side2
        self.side3 = side3

    def is_equilateral(self):
        return self.side1 == self.side2 == self.side3

    def area(self):
        if self.is_equilateral():
            return math.sqrt(3) / 4 * self.side1 ** 2
        else:
            s = (self.side1 + self.side2 + self.side3) / 2
            return math.sqrt(s * (s - self.side1) * (s - self.side2) * (s - self.side3))

def calculate_area_ratio(triangle1, triangle2):
    area1 = triangle1.area()
    area2 = triangle2.area()
    if area2 == 0:
        return float('inf')
    return area1 / area2
if __name__ == '__main__':
    equilateral_triangle = Triangle(5, 5, 5)
    isosceles_triangle = Triangle(5, 5, 8)
    ratio = calculate_area_ratio(equilateral_triangle, isosceles_triangle)
    print(ratio)