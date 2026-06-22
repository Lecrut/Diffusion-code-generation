import math

def cone_volume(radius, height):
    return (math.pi * radius**2 * height) / 3

if __name__ == '__main__':
    result = cone_volume(1, 3)
    print(result)