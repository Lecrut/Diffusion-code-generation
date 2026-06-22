import math

PI_CONSTANT = math.pi
ONE_THIRD_CONSTANT = 1 / 3

def cone_volume(radius: float, height: float) -> float:
    base_area = PI_CONSTANT * (radius ** 2)
    return ONE_THIRD_CONSTANT * base_area * height

if __name__ == '__main__':
    sample_radius = 7.0
    sample_height = 12.0
    volume = cone_volume(sample_radius, sample_height)
    print(volume)