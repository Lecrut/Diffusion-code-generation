class Cuboid:
    def __init__(self, length, width, height):
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.length = length
        self.width = width
        self.height = height

    def compute_surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

if __name__ == '__main__':
    try:
        box = Cuboid(10, 20, 30)
        print(box.compute_surface_area())
    except ValueError as e:
        print(e)