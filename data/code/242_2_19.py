PI = 3.14
WIDTH = 5
HEIGHT = 10

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return PI * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height

def compare_areas(circle, rectangle):
    circle_area = circle.area()
    rectangle_area = rectangle.area()
    if circle_area > rectangle_area:
        return "Circle is larger"
    elif circle_area < rectangle_area:
        return "Rectangle is larger"

if __name__ == '__main__':
    circle = Circle(3)
    rectangle = Rectangle(WIDTH, HEIGHT)
    result = compare_areas(circle, rectangle)
    print(result)