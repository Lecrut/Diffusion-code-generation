import math

class Triangle:
    def __init__(self, base=None, height=None):
        self.base = base
        self.height = height

    def area(self):
        raise ValueError("This method should be overridden by subclasses")

class EquilateralTriangle(Triangle):
    def __init__(self, side_length):
        super().__init__()
        self.side_length = side_length

    def area(self):
        return (math.sqrt(3) / 4) * self.side_length ** 2

class IsoscelesTriangle(Triangle):
    def __init__(self, base, height):
        super().__init__(base, height)

    def area(self):
        return 0.5 * self.base * self.height

def ratio_of_areas(equilateral_side, isosceles_base, isosceles_height):
    equilateral = EquilateralTriangle(equilateral_side)
    isosceles = IsoscelesTriangle(isosceles_base, isosceles_height)
    
    if isosceles.area() == 0:
        raise ZeroDivisionError("Isosceles triangle area cannot be zero for ratio calculation")
    
    return equilateral.area() / isosceles.area()

if __name__ == '__main__':
    equilateral_side_length = 6.0
    isosceles_base_length = 8.0
    isosceles_height_length = 5.0
    ratio = ratio_of_areas(equilateral_side_length, isosceles_base_length, isosceles_height_length)
    print(ratio)