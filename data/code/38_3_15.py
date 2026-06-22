import math

def cone_volume(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    base_area = math.pi * radius ** 2
    return base_area * height / 3

if __name__ == '__main__':
    print(cone_volume(4, 12))