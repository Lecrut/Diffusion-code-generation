import math

class Circle:
    PI = 3.141592653589793
    
    def __init__(self, radius: float):
        self.radius = radius
    
    @staticmethod
    def area(radius: float) -> float:
        return Circle.PI * (radius ** 2)
    
if __name__ == '__main__':
    circle1 = Circle(5.0)
    area1 = circle1.area()
    print(f"Area of circle with radius 5.0: {area1}")