class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * (self.radius ** 2)

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
    else:
        return "Both shapes have the same area"

if __name__ == '__main__':
    circle = Circle(5)
    rectangle = Rectangle(4, 6)
    print(compare_areas(circle, rectangle))