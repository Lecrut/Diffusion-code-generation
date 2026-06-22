import math

CONES_BASE_RADIUS = 5.0
CONES_HEIGHT = 10.0

def calculate_cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    volume = calculate_cone_volume(CONES_BASE_RADIUS, CONES_HEIGHT)
    print(volume)