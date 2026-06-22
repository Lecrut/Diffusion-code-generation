import math

def compute_cone_volume(radius, height):
    return math.pi * (radius ** 2) * height / 3

if __name__ == '__main__':
    radius = 1
    height = 3
    volume = compute_cone_volume(radius, height)
    print(volume)