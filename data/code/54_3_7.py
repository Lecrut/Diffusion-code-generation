import math

def get_area(radius: float) -> float:
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    return math.pi * (radius ** 2)

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return get_area(self.radius)

if __name__ == '__main__':
    try:
        circle1 = Circle(5.0)
        print(f"The area of a circle with radius {circle1.radius} is: {circle1.area()}")
        
        circle2 = Circle(0.5)
        print(f"The area of a circle with radius {circle2.radius} is: {circle2.area()}")
        
        circle3 = Circle(10.5)
        print(f"The area of a circle with radius {circle3.radius} is: {circle3.area()}")
    except ValueError as e:
        print(e)