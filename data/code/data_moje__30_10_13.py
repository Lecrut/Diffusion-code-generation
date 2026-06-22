import math

class CircleAreaCalculator:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius must be non-negative")
        self.radius = radius
        self.pi = math.pi

    def compute_area(self):
        return self.pi * self.radius ** 2

    def display_info(self):
        return f"Radius: {self.radius}, Area: {self.compute_area()}"

if __name__ == '__main__':
    calc1 = CircleAreaCalculator(5)
    calc2 = CircleAreaCalculator(10.5)
    print(calc1.compute_area())
    print(calc2.compute_area())
    print(calc1.display_info())
    print(calc2.display_info())