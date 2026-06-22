import math

class Circle:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return math.pi * (self.radius ** 2)

if __name__ == '__main__':
    sample_values = {
        'circle1': {'radius': 3.0},
        'circle2': {'radius': 4.5},
        'circle3': {'radius': 7.0}
    }
    
    for name, data in sample_values.items():
        circle = Circle(data['radius'])
        print(f"The area of {name} with radius {data['radius']} is: {circle.area()}")