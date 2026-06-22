import math

def compute_cone_volume(radius, height):
    volume = (1 / 3) * math.pi * (radius ** 2) * height
    return volume

if __name__ == '__main__':
    r = 5
    h = 10
    result = compute_cone_volume(r, h)
    print(result)