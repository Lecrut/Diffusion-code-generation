import math

def calculate_cone_volume(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError('Radius and height must be non-negative')
    volume = 1 / 3 * math.pi * radius ** 2 * height
    return volume
if __name__ == '__main__':
    radius = 5
    height = 10
    volume = calculate_cone_volume(radius, height)
    print(volume)