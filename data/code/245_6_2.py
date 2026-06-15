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
    print("Circle comparison:")
    area_c1 = circle1.get_area()
    area_c2 = circle2.get_area()
    print(f"Area of Circle 1: {area_c1}")
    print(f"Area of Circle 2: {area_c2}")
    print(f"Areas are equal: {area_c1 == area_c2}")
    print("\nRectangle comparison:")
    area_r1 = rectangle1.get_area()
    area_r2 = rectangle2.get_area()
    print(f"Area of Rectangle 1: {area_r1}")
    print(f"Area of Rectangle 2: {area_r2}")
    print(f"Areas are equal: {area_r1 == area_r2}")
    print("\nTriangle comparison:")
    area_t1 = triangle1.get_area()
    area_t2 = triangle2.get_area()
    print(f"Area of Triangle 1: {area_t1}")
    print(f"Area of Triangle 2: {area_t2}")
    print(f"Areas are equal: {area_t1 == area_t2}")