class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.141592653589793 * self.radius ** 2
if __name__ == '__main__':
    circle1 = Circle(5)
    area1 = circle1.area()
    print(f"Area of circle with radius 5: {area1}")
    circle2 = Circle(10.5)
    area2 = circle2.area()
    print(f"Area of circle with radius 10.5: {area2}")