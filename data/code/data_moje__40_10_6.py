class RectangularBox:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height

    def calculate_surface_area(self):
        return 2 * (self.area_pair(self.length, self.width) + self.area_pair(self.width, self.height) + self.area_pair(self.height, self.length))

    @staticmethod
    def area_pair(a, b):
        return a * b

if __name__ == '__main__':
    box = RectangularBox(10, 5, 3)
    print(box.calculate_surface_area())