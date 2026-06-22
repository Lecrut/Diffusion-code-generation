import math

CONE_HEIGHT = 10.0
BASE_RADIUS = 5.0

def calculate_cone_volume(height, radius):
    if height <= 0 or radius <= 0:
        raise ValueError("Height and radius must be positive numbers")
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    volume = calculate_cone_volume(CONE_HEIGHT, BASE_RADIUS)
    print(volume)