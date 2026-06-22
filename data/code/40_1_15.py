def compute_surface_area(length, width, height):
    return 2 * (length * width + length * height + width * height)

class RectangularPrism:
    def __init__(self, length, width, height):
        self.length = length
        self.width = width
        self.height = height
    
    def get_surface_area(self):
        return 2 * (self.length * self.width + self.length * self.height + self.width * self.height)

if __name__ == '__main__':
    print(compute_surface_area(5.0, 3.0, 2.0))
    prism = RectangularPrism(5.0, 3.0, 2.0)
    print(prism.get_surface_area())