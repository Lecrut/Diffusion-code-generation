import math

def cone_volume(radius, height):
    return (1/3) * math.pi * radius ** 2 * height

if __name__ == '__main__':
    r = 5.0
    h = 10.0
    print(cone_volume(r, h))