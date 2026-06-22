import math

class ConeCalculator:
    PI = math.pi

    @staticmethod
    def get_volume(radius: float, height: float) -> float:
        return (1.0 / 3.0) * ConeCalculator.PI * (radius ** 2) * height

if __name__ == '__main__':
    RADIUS_VAL = 3.0
    HEIGHT_VAL = 9.0
    print(ConeCalculator.get_volume(RADIUS_VAL, HEIGHT_VAL))