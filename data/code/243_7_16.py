class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius

    def calculate_circumference(self):
        return 2 * 3.14159 * self.radius

if __name__ == '__main__':
    circle_instance = Circle(7)
    print(f"Circumference of the circle with radius {circle_instance.radius}: {circle_instance.calculate_circumference()}")