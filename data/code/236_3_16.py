class CircularShape:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        import math
        return math.pi * self.radius ** 2

def circular_shape_generator(radius, count):
    for _ in range(count):
        yield CircularShape(radius)

if __name__ == '__main__':
    shapes = list(circular_shape_generator(5, 3))
    print(shapes[0].area())