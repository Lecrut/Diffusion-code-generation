import math

def calculate_cone_volume(radius, height):
    if radius <= 0 or height <= 0:
        return 0.0
    return math.pi * radius * radius * height / 3.0

if __name__ == '__main__':
    r = 3
    h = 7
    print(calculate_cone_volume(r, h))