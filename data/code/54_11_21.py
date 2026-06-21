import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius ** 2

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return calculate_circle_area(self.radius)

if __name__ == '__main__':
    sample_values = {
        'small': 1.0,
        'medium': 5.0,
        'large': 10.0
    }
    
    for description, radius in sample_values.items():
        circle = Circle(radius)
        print(f"The area of a {description} circle with radius {radius} is {circle.area()}")