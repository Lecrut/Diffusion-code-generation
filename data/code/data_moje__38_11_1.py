import math

RADIUS = 5.0
HEIGHT = 12.0

def calculate_cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    volume = calculate_cone_volume(RADIUS, HEIGHT)
    print(volume)