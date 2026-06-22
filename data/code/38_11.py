import math

def cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    RADIUS = 5.0
    HEIGHT = 10.0
    volume = cone_volume(RADIUS, HEIGHT)
    print(volume)