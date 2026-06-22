import math

def calculate_cone_volume(radius, height):
    volume = (1/3) * math.pi * (radius ** 2) * height
    return volume

if __name__ == '__main__':
    RADIUS = 5
    HEIGHT = 10
    result = calculate_cone_volume(RADIUS, HEIGHT)
    print(result)