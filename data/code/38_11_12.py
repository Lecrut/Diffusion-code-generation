import math

class ConeDimensions:
    radius = 7.5
    height = 12.0

    @staticmethod
    def compute_base_area(r):
        return math.pi * (r ** 2)

    @staticmethod
    def compute_volume(radius, height):
        base_area = ConeDimensions.compute_base_area(radius)
        return (1.0 / 3.0) * base_area * height

if __name__ == '__main__':
    r = ConeDimensions.radius
    h = ConeDimensions.height
    volume = ConeDimensions.compute_volume(r, h)
    print(volume)