import math

def cone_volume(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    radius = 1
    height = 3
    print(cone_volume(radius, height))