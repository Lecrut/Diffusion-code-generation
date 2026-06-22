import math

def compute_cone_volume(radius, height):
    base_area = math.pi * (radius ** 2)
    volume = (1 / 3) * base_area * height
    return volume

if __name__ == '__main__':
    radius = 5
    height = 10
    result = compute_cone_volume(radius, height)
    print(result)