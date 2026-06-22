import math

class ConeCalculator:
    PI = math.pi
    FRACTION = 1 / 3

    @staticmethod
    def compute_volume(radius, height):
        return ConeCalculator.FRACTION * ConeCalculator.PI * radius ** 2 * height

if __name__ == '__main__':
    calculator = ConeCalculator()
    volume = calculator.compute_volume(10, 20)
    print(volume)