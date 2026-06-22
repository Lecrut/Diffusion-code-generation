class CircularShape:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

def circular_shape_generator(radius, iterations):
    for _ in range(iterations):
        yield CircularShape(radius)

if __name__ == '__main__':
    generator = circular_shape_generator(5, 3)
    shapes = list(generator)
    for shape in shapes:
        print(shape.area())