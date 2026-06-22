class CircularShape:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

def circular_shape_generator(radius, iterations):
    for _ in range(iterations):
        yield CircularShape(radius)

if __name__ == '__main__':
    generator = circular_shape_generator(7, 5)
    for shape in generator:
        print(f"Area of circle with radius {shape.radius}: {shape.area()}")