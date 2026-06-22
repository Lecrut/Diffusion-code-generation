class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius ** 2

def circle_generator(radius, count):
    for _ in range(count):
        yield Circle(radius)

if __name__ == '__main__':
    gen = circle_generator(7, 4)
    circles = list(gen)
    print([c.area() for c in circles])