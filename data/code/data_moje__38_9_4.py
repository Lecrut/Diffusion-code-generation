import math

ONE_THIRD = 1 / 3

def calculate_cone_volume(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    return ONE_THIRD * math.pi * radius * radius * height

if __name__ == '__main__':
    print(calculate_cone_volume(10, 20))