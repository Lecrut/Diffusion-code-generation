import math

def volume_of_cone(radius, height):
    return (1 / 3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    radius = 3.0
    height = 5.0
    result = volume_of_cone(radius, height)
    print(result)