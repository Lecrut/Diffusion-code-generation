class CircularShape:
    PI = 3.14
    
    def __init__(self, radius):
        self.radius = radius
    
    @staticmethod
    def area(radius):
        return CircularShape.PI * radius ** 2

def circular_shape_generator(radius, iterations):
    for _ in range(iterations):
        yield CircularShape(radius)

if __name__ == '__main__':
    generator = circular_shape_generator(5, 3)
    for shape in generator:
        print(shape.area())