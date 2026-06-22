class Box:
    def __init__(self, dimensions):
        self.dimensions = dimensions
    def surface_area(self):
        return 2 * sum([a * b for a, b in zip(self.dimensions, self.dimensions[1:]) + [self.dimensions[:1]] * self.dimensions[-1:]])

if __name__ == '__main__':
    box = Box([4, 6, 8])
    print(box.surface_area())