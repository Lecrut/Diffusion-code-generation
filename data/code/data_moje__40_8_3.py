class BoxSurfaceCalculator:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def get_surface_area(self):
        if not isinstance(self.length, (int, float)) or self.length <= 0:
            raise ValueError("Length must be a positive number")
        if not isinstance(self.width, (int, float)) or self.width <= 0:
            raise ValueError("Width must be a positive number")
        if not isinstance(self.height, (int, float)) or self.height <= 0:
            raise ValueError("Height must be a positive number")
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

if __name__ == '__main__':
    box = BoxSurfaceCalculator(7, 5, 3)
    print(box.get_surface_area())