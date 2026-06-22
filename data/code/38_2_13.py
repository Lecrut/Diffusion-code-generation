import math

class ConeGeometry:
    RADIUS_CONST = 3
    HEIGHT_CONST = 7

    @staticmethod
    def compute_volume(r, h):
        return (1 / 3) * math.pi * (r ** 2) * h

if __name__ == '__main__':
    vol = ConeGeometry.compute_volume(ConeGeometry.RADIUS_CONST, ConeGeometry.HEIGHT_CONST)
    print(vol)