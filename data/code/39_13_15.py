class PrismCalculator:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height

    def volume(self):
        return self.base_area * self.height

    def surface_area_rectangular(self):
        return 2 * (self.base_area + self.base_area + self.base_area)

if __name__ == '__main__':
    prism = PrismCalculator(base_area=12.0, height=7.5)
    print(prism.volume())
    print(prism.surface_area_rectangular())