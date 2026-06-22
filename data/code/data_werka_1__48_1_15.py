class Shape:
    def __init__(self, length, width=None):
        self.length = length
        self.width = width if width is not None else length

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

if __name__ == '__main__':
    shapes = {
        'square': Shape(5),
        'rectangle': Shape(4, 6)
    }

    for shape_name, shape in shapes.items():
        print(f"{shape_name.capitalize()} Perimeter: {shape.perimeter()}")
        print(f"{shape_name.capitalize()} Area: {shape.area()}")