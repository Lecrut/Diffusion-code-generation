import math

class Circle:
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)
    
    def diameter(self):
        return 2 * self.radius

if __name__ == '__main__':
    try:
        sample_radius = 8.0
        circle = Circle(sample_radius)
        print(f"Area: {circle.area()}")
        print(f"Diameter: {circle.diameter()}")
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")