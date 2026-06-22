import math

class Circle:
    PI = math.pi

    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return self.PI * (self.radius ** 2)

if __name__ == '__main__':
    sample_values = [
        {'radius': 1.5},
        {'radius': 3.7},
        {'radius': 6.0}
    ]
    for data in sample_values:
        circle = Circle(data['radius'])
        print(f"The area of a circle with radius {data['radius']} is: {circle.area()}")