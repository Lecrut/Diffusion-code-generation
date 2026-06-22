import math

def cone_volume(radius: float, height: float) -> float:
    return (1 / 3) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    sample_radius = 5.0
    sample_height = 10.0
    volume = cone_volume(sample_radius, sample_height)
    print(volume)