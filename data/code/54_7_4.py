class Circle:
    def __init__(self, radius):
        self.radius = radius
    def calculate_area(self):
        return 3.14159 * self.radius ** 2
    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius
if __name__ == '__main__':
    circle1 = Circle(5)
    print(f"Area of circle 1: {circle1.calculate_area()}")
    print(f"Circumference of circle 1: {circle1.calculate_circumference()}")
    circle2 = Circle(10)
    print(f"Area of circle 2: {circle2.calculate_area()}")
    print(f"Circumference of circle 2: {circle2.calculate_circumference()}")