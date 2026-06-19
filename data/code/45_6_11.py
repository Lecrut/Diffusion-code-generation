import math

def calculate_circle_area(radius):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * radius**2

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return calculate_circle_area(self.radius)

if __name__ == '__main__':
    test_cases = [
        (1, math.pi),
        (2, 4 * math.pi),
        (0, 0),
        (5, 25 * math.pi)
    ]
    
    for radius, expected in test_cases:
        try:
            circle = Circle(radius)
            result = circle.area()
            assert math.isclose(result, expected), f"Input radius: {radius}, Expected: {expected}, Got: {result}"
            print(f"Test passed for radius: {radius}")
        except ValueError as e:
            print(e)

    try:
        Circle(-1).area()
    except ValueError as e:
        print(e)