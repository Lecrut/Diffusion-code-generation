import math

PI_CONST = math.pi
DIVISOR_THREE = 3

class ConeVolumeCalculator:
    def __init__(self, radius, height):
        self.radius = radius
        self.height = height

    def compute_volume(self):
        base_area = PI_CONST * self.radius * self.radius
        return base_area * self.height / DIVISOR_THREE

if __name__ == '__main__':
    SAMPLE_RADIUS = 7
    SAMPLE_HEIGHT = 5
    calculator = ConeVolumeCalculator(SAMPLE_RADIUS, SAMPLE_HEIGHT)
    print(calculator.compute_volume())