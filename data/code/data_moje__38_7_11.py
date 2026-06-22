class ConeVolumeCalculator:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height
        self.pi_value = 3.141592653589793

    def get_base_area(self):
        return self.pi_value * (self.radius ** 2)

    def get_volume(self):
        base_area = self.get_base_area()
        return (base_area * self.height) / 3.0

if __name__ == '__main__':
    calc = ConeVolumeCalculator(7, 5)
    print(calc.get_base_area())
    print(calc.get_volume())