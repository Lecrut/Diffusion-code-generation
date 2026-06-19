import math

class RightAngledTriangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height
        self.hypotenuse = self._calculate_hypotenuse()
    
    def _calculate_hypotenuse(self):
        return math.sqrt(self.base ** 2 + self.height ** 2)
    
    def get_side_lengths(self):
        return self.base, self.height, self.hypotenuse
    
    def calculate_area(self):
        return (self.base * self.height) / 2

if __name__ == '__main__':
    triangle = RightAngledTriangle(6.0, 8.0)
    print(triangle.get_side_lengths())
    print(triangle.calculate_area())