class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

class Rectangle:
    def __init__(self, width, height):
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
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
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print(compare_areas(circle, rectangle))