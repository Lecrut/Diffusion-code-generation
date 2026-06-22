import math

def calculate_circle_perimeter(radius):
    return 2 * math.pi * radius

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def get_radius(self):
        return self.radius
    
    def set_radius(self, new_radius):
        self.radius = new_radius
    
    def perimeter(self):
        return calculate_circle_perimeter(self.radius)

if __name__ == '__main__':
    sample_circle = Circle(5.0)
    print("Original Radius:", sample_circle.get_radius())
    print("Perimeter:", sample_circle.perimeter())
    sample_circle.set_radius(7.5)
    print("Updated Radius:", sample_circle.get_radius())
    print("New Perimeter:", sample_circle.perimeter())