import math

def cone_volume(radius, height):
    return (math.pi * radius ** 2 * height) / 3

if __name__ == '__main__':
    r = 1
    h = 3
    result = cone_volume(r, h)
    print(result)