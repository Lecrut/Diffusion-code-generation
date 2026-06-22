class RectangularBox:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_surface_area(self):
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def get_volume(self):
        return self.length * self.width * self.height

    def get_dimensions(self):
        return (self.length, self.width, self.height)

if __name__ == '__main__':
    box = RectangularBox(10, 5, 3)
    area = box.calculate_surface_area()
    volume = box.get_volume()
    dims = box.get_dimensions()
    print(area)
    print(volume)
    print(dims)