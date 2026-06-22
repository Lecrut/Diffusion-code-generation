from math import pi

class ConeVolumeCalculator:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def calculate_volume(self):
        return (1.0 / 3.0) * pi * (self.radius ** 2) * self.height

def get_predefined_dimensions():
    return 5.0, 10.0

if __name__ == '__main__':
    radius_value, height_value = get_predefined_dimensions()
    calculator = ConeVolumeCalculator(radius_value, height_value)
    volume = calculator.calculate_volume()
    print(volume)