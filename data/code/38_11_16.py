import math

BASE_HEIGHT = 5.0
BASE_RADIUS = 3.0

def calculate_cone_volume(radius, height):
    return (math.pi * (radius ** 2) * height) / 3.0

if __name__ == '__main__':
    result = calculate_cone_volume(BASE_RADIUS, BASE_HEIGHT)
    print(result)