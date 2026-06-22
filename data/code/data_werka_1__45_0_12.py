import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius

    def area(self):
        return math.pi * self.radius ** 2

    def circumference(self):
        return 2 * math.pi * self.radius

def calculate_circle_area(radius):
    circle = Circle(radius)
    return circle.area()

if __name__ == '__main__':
    sample_radius = 4.0
    try:
        area = calculate_circle_area(sample_radius)
        print(f"Area: {area}")
        
        circle_instance = Circle(sample_radius)
        circumference = circle_instance.circumference()
        print(f"Circumference: {circumference}")
    except ValueError as e:
        print(e)