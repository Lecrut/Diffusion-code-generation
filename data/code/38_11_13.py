import math

def cone_volume(radius: float, height: float) -> float:
    return (math.pi * radius ** 2 * height) / 3.0

if __name__ == '__main__':
    RADIUS = 5.0
    HEIGHT = 10.0
    volume = cone_volume(RADIUS, HEIGHT)
    print(volume)