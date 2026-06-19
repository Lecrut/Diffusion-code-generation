import math
PI = math.pi

class Circle:

    def __init__(self, radius):
        self.radius = radius
        if self.radius < 0:
            raise ValueError('Radius cannot be negative')

    def area(self):
        return PI * self.radius ** 2

def calculate_circle_area(radius):
    return Circle(radius).area()
if __name__ == '__main__':
    sample_radius = 10.0
    try:
        computed_area = calculate_circle_area(sample_radius)
        print(computed_area)
    except ValueError as e:
        print(e)