import math

def cone_volume(radius, height):
    return math.pi * radius ** 2 * height / 3

if __name__ == '__main__':
    result = cone_volume(8, 11)
    print(f"{result:.2f}")