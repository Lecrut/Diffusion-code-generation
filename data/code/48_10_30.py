import math

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def calculate_perimeter(self):
        return 2 * (self.width + self.height)
    
    def calculate_area(self):
        return self.width * self.height

def main():
    rect = Rectangle(7.0, 4.5)
    perimeter = rect.calculate_perimeter()
    area = rect.calculate_area()
    print(f"Perimeter: {perimeter}")
    print(f"Area: {area}")

if __name__ == '__main__':
    main()