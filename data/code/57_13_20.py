class GeometryCalculator:
    def __init__(self):
        self.shapes = {}

    def add_shape(self, name, shape):
        self.shapes[name] = shape

    def get_shape_area(self, name):
        if name in self.shapes:
            return self.shapes[name].area()
        raise ValueError("Shape not found.")

class Triangle:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def area(self):
        return 0.5 * self.base * self.height

if __name__ == '__main__':
    calculator = GeometryCalculator()
    triangle = Triangle(6, 8)
    calculator.add_shape('triangle', triangle)
    
    print("Triangle Area:", calculator.get_shape_area('triangle'))