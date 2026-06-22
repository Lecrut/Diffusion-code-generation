class CircularShape:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

def circular_shape_generator(radius, iterations):
    shape = CircularShape(radius)
    for _ in range(iterations):
        yield shape

if __name__ == '__main__':
    generator = circular_shape_generator(5, 3)
    for _ in range(3):
        print(next(generator).area())