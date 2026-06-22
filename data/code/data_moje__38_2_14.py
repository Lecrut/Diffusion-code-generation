import math

def compute_cone_volume(radius, height):
    return (1.0 / 3.0) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    radius = 3
    height = 7
    result = compute_cone_volume(radius, height)
    print(result)