class BoxSurfaceArea:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate(self):
        if self.length <= 0 or self.width <= 0 or self.height <= 0:
            raise ValueError('Dimensions must be positive numbers.')
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

if __name__ == '__main__':
    dimensions = (7, 3, 4)
    box = BoxSurfaceArea(*dimensions)
    print(box.calculate())