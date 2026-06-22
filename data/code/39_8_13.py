class PrismVolumeCalculator:
    def __init__(self, base_area, height):
        self.base_area = base_area
        self.height = height
        self.volume = base_area * height

    def get_volume(self):
        return self.volume

    def get_base_area(self):
        return self.base_area

    def get_height(self):
        return self.height

    def scale(self, factor):
        self.base_area *= factor
        self.height *= factor
        self.volume = self.base_area * self.height
        return self.get_volume()

if __name__ == '__main__':
    calc = PrismVolumeCalculator(15.5, 4.0)
    print(calc.get_volume())
    print(calc.get_base_area())
    print(calc.get_height())
    print(calc.scale(2.0))