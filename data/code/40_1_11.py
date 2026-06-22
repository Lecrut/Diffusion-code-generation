class RectangularPrism:
    def __init__(self, length: float, width: float, height: float) -> None:
        if length <= 0 or width <= 0 or height <= 0:
            raise ValueError("Dimensions must be positive")
        self.length = length
        self.width = width
        self.height = height

    def calculate_surface_area(self) -> float:
        return 2.0 * (self.length * self.width + self.width * self.height + self.height * self.length)

if __name__ == '__main__':
    dimensions = (5.0, 3.0, 2.0)
    prism = RectangularPrism(*dimensions)
    print(prism.calculate_surface_area())