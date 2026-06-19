import math

class Circle:
    PI = math.pi
    
    def __init__(self, radius):
        if radius <= 0:
            raise ValueError("Radius must be a positive number.")
        self.radius = radius
    
    @staticmethod
    def calculate_area(radius):
        return Circle.PI * (radius ** 2)
    
    def area(self):
        return Circle.calculate_area(self.radius)

if __name__ == '__main__':
    try:
        sample_radius = 3.5
        circle = Circle(sample_radius)
        print(circle.area())
    except ValueError as e:
        print(e)
    except Exception as e:
        print(f"An unexpected error occurred: {e}")