import math

class Circle:
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    circle1 = Circle(5.0)
    print(f"The area of a circle with radius {circle1.radius} is {circle1.area()}")
    
    circle2 = Circle(2.5)
    print(f"The area of a circle with radius {circle2.radius} is {circle2.area()}")
    
    circle3 = Circle(0.0)
    print(f"The area of a circle with radius {circle3.radius} is {circle3.area()}")