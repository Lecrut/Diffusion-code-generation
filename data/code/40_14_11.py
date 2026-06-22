class RectangularBox:
    def __init__(self, length: float, width: float, height: float) -> None:
        self.length = length
        self.width = width
        self.height = height

    def surface_area(self) -> float:
        return 2 * (self.length * self.width + self.width * self.height + self.height * self.length)

    def volume(self) -> float:
        return self.length * self.width * self.height

    def dimensions(self) -> tuple:
        return (self.length, self.width, self.height)

if __name__ == '__main__':
    box = RectangularBox(2.5, 3.0, 4.0)
    print(box.surface_area())
    print(box.volume())
    print(box.dimensions())