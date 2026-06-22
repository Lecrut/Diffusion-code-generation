class Circle:
    PI = 3.141592653589793

    def __init__(self, radius):
        self.radius = radius

    def _validate_radius(self):
        if not isinstance(self.radius, (int, float)):
            raise TypeError("Radius must be a number.")
        if self.radius < 0:
            raise ValueError("Radius cannot be negative.")

    def calculate_area(self):
        self._validate_radius()
        return self.PI * self.radius ** 2

if __name__ == '__main__':
    circle = Circle(5.0)
    area = circle.calculate_area()
    print(area)