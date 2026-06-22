class Circle:
    PI = 3.14

    def __init__(self, radius):
        self.radius = radius

    @staticmethod
    def area(radius):
        return Circle.PI * radius ** 2

class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @staticmethod
    def area(width, height):
        return width * height

def compare_areas(circle, rectangle):
    circle_area = Circle.area(circle.radius)
    rectangle_area = Rectangle.area(rectangle.width, rectangle.height)

    if circle_area > rectangle_area:
        return "Circle is larger"
    elif circle_area < rectangle_area:
        return "Rectangle is larger"

if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print(compare_areas(circle, rectangle))