class RectangularBox:
    def __init__(self, length, width, height):
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.length = length
        self.width = width
        self.height = height

    def get_surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

if __name__ == '__main__':
    box = RectangularBox(10, 8, 6)
    print(box.get_surface_area())