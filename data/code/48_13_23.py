import math

class RightTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def hypotenuse(self):
        return math.sqrt(self.base**2 + self.height**2)
    
    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    triangle = RightTriangle(6.0, 8.0)
    print(f"Hypotenuse: {triangle.hypotenuse()}")
    print(f"Area: {triangle.area()}")