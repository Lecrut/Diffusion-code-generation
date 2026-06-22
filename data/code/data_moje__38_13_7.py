import math

def cone_volume(radius, height):
    return (1 / 3) * math.pi * radius**2 * height

if __name__ == '__main__':
    radius = 5
    height = 10
    result = cone_volume(radius, height)
    print(result)