import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def perimeter(self):
        return 2 * (self.width + self.height)
    
    def area(self):
        return self.width * self.height

if __name__ == '__main__':
    rect = Rectangle(5.0, 3.0)
    print(rect.perimeter())
    print(rect.area())