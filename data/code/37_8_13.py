class Parallelogram:
    def __init__(self, base, height):
        self.base = base
        self.height = height

    def get_area(self):
        return self.base * self.height

    def get_dimensions(self):
        return self.base, self.height

if __name__ == '__main__':
    shape = Parallelogram(7, 4)
    dims = shape.get_dimensions()
    area = shape.get_area()
    print(f"Dimensions: {dims[0]}x{dims[1]}")
    print(area)