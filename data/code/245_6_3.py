class Shape:
    def get_area(self):
        raise NotImplementedError
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    def get_area(self):
        return 3.14159 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self, width, height):
        self.width = width
        self.height = height
    def get_area(self):
        return self.width * self.height
class Triangle(Shape):
    def __init__(self, base, height):
        self.base = base
        self.height = height
    def get_area(self):
        return 0.5 * self.base * self.height
if __name__ == '__main__':
    circle1 = Circle(5)
    circle2 = Circle(5)
    rectangle1 = Rectangle(4, 6)
    rectangle2 = Rectangle(4, 6)
    triangle1 = Triangle(10, 5)
    triangle2 = Triangle(10, 5)
    print("Comparing Circles:")
    if circle1.get_area() == circle2.get_area():
        print("Circle areas are equal.")
    else:
        print("Circle areas are not equal.")
    print("\nComparing Rectangles:")
    if rectangle1.get_area() == rectangle2.get_area():
        print("Rectangle areas are equal.")
    else:
        print("Rectangle areas are not equal.")
    print("\nComparing Triangles:")
    if triangle1.get_area() == triangle2.get_area():
        print("Triangle areas are equal.")
    else:
        print("Triangle areas are not equal.")