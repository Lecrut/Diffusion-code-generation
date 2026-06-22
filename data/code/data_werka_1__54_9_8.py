import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius_1 = 3.5
    sample_radius_2 = 6.0
    circle1 = Circle(sample_radius_1)
    circle2 = Circle(sample_radius_2)
    
    area_circle1 = circle1.area()
    area_circle2 = circle2.area()
    
    print(f"The area of the first circle with radius {sample_radius_1} is: {area_circle1}")
    print(f"The area of the second circle with radius {sample_radius_2} is: {area_circle2}")