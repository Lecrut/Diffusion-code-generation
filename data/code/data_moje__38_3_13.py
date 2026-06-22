import math

def cone_volume(radius, height):
    return (1/3) * math.pi * radius**2 * height

if __name__ == '__main__':
    r = 4
    h = 12
    result = cone_volume(r, h)
    print(result)