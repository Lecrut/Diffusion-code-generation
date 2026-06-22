import math

def volume_cone(radius, height):
    return (1/3) * math.pi * radius**2 * height

if __name__ == '__main__':
    r = 1
    h = 3
    result = volume_cone(r, h)
    print(result)