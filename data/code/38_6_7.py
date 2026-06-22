import math

def cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    print(cone_volume(1, 3))