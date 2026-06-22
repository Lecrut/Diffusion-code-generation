class CircularShape:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

def circular_shape_generator(radius, iterations):
    for _ in range(iterations):
        yield CircularShape(radius)

if __name__ == '__main__':
    gen = circular_shape_generator(5, 3)
    print(next(gen).area())
    print(next(gen).area())
    print(next(gen).area())