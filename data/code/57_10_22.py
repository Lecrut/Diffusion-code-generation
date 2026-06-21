import math

def compute_area_of_circle(radius):
    return math.pi * (radius ** 2)

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return compute_area_of_circle(self.radius)

if __name__ == '__main__':
    sample_radius = 5
    circle_instance = Circle(sample_radius)
    print(circle_instance.area())