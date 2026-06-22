import math

def compute_cone_volume(radius, height):
    return (1/3) * math.pi * (radius ** 2) * height

if __name__ == '__main__':
    r = 3
    h = 7
    result = compute_cone_volume(r, h)
    print(result)