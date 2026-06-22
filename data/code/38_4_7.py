import math

def calculate_cone_volume(r, h):
    return (1 / 3) * math.pi * r ** 2 * h

if __name__ == '__main__':
    radius = 6
    height = 9
    volume = calculate_cone_volume(radius, height)
    print(volume)