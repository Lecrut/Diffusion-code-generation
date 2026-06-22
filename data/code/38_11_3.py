import math

CONST_RADIUS = 5.0
CONST_HEIGHT = 10.0

def calculate_cone_volume(radius, height):
    return (1 / 3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    volume = calculate_cone_volume(CONST_RADIUS, CONST_HEIGHT)
    print(volume)