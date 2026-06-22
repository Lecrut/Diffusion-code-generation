import math

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def perimeter(self):
        return 2 * math.pi * self.radius

def calculate_circle_perimeter(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return 2 * math.pi * radius

if __name__ == '__main__':
    try:
        circle = Circle(radius=8)
        print(circle.perimeter())
    except ValueError as e:
        print(e)

    try:
        perimeter_value = calculate_circle_perimeter(12)
        print(perimeter_value)
    except ValueError as e:
        print(e)