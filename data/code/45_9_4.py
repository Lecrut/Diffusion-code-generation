import math

PI = math.pi

class Circle:
    def __init__(self, radius):
        if radius < 0:
            raise ValueError("Radius cannot be negative")
        self.radius = radius
    
    def area(self):
        return PI * self.radius ** 2
    
    def circumference(self):
        return 2 * PI * self.radius

if __name__ == '__main__':
    try:
        sample_radius1 = 5.0
        circle1 = Circle(sample_radius1)
        print("Area of circle with radius", sample_radius1, "is:", circle1.area())
        print("Circumference of circle with radius", sample_radius1, "is:", circle1.circumference())
        
        sample_radius2 = 10.0
        circle2 = Circle(sample_radius2)
        print("Area of circle with radius", sample_radius2, "is:", circle2.area())
        print("Circumference of circle with radius", sample_radius2, "is:", circle2.circumference())
        
    except ValueError as e:
        print(e)