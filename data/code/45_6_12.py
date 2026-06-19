import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    test_cases = [
        Circle(1),
        Circle(2),
        Circle(0),
        Circle(10),
        Circle(5.5)
    ]
    for circle in test_cases:
        print(f"Radius: {circle.radius}, Area: {circle.area()}")