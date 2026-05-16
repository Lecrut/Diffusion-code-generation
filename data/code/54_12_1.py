class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * self.radius * self.radius
if __name__ == '__main__':
    circle1 = Circle(5)
    area1 = circle1.calculate_area()
    print(area1)
    circle2 = Circle(10.5)
    area2 = circle2.calculate_area()
    print(area2)