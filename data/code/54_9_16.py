import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_radius = 6.0
    circle_instance = Circle(sample_radius)
    calculated_area = circle_instance.area()
    print(f"The area of the circle with radius {sample_radius} is: {calculated_area}")