import math

def cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

if __name__ == '__main__':
    print(cone_volume(4, 12))