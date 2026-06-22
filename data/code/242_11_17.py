class Shape:
    def calculate_area(self):
        return 0

class Square(Shape):
    def __init__(self, side):
        self.side = side
    
    def calculate_area(self):
        return self.side ** 2

class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    
    def calculate_area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    square = Square(4)
    triangle = Triangle(5, 6)
    
    print(square.calculate_area() > triangle.calculate_area())