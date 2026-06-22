import math

def cone_volume(radius, height):
    base_area = math.pi * radius ** 2
    return base_area * height / 3

if __name__ == '__main__':
    print(cone_volume(6, 9))