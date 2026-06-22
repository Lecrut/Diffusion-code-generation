class CircularShape:
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius ** 2

def validate_radius(radius):
    if not isinstance(radius, (int, float)) or radius <= 0:
        raise ValueError("Radius must be a positive number")

def validate_iterations(iterations):
    if not isinstance(iterations, int) or iterations < 0:
        raise ValueError("Iterations must be a non-negative integer")

def circular_shape_generator(radius, iterations):
    validate_radius(radius)
    validate_iterations(iterations)
    for _ in range(iterations):
        yield CircularShape(radius)

if __name__ == '__main__':
    generator = circular_shape_generator(5, 3)
    for shape in generator:
        print(f"Area: {shape.area()}")