import math

class Shape:
    def area(self):
        return 0.0

class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

def calculate_total_area(shapes):
    total = 0.0
    for shape in shapes:
        total += shape.area()
    return total

if __name__ == '__main__':
    rect_instance = Rectangle(12, 8)
    circle_instance = Circle(5)
    
    rect_area = rect_instance.area()
    circle_area = circle_instance.area()
    
    print(rect_area)
    print(circle_area)
    
    collection = [rect_instance, circle_instance]
    total_area = calculate_total_area(collection)
    print(total_area)