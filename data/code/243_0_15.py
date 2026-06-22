import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def calculate_circumference(self) -> float:
        return 2 * math.pi * self.radius

if __name__ == '__main__':
    circle_instance = Circle(5.0)
    circumference = circle_instance.calculate_circumference()
    print(circumference)