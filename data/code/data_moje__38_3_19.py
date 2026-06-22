import math

def calculate_cone_volume(radius, height):
    base_area = math.pi * radius ** 2
    volume = (base_area * height) / 3
    return volume

if __name__ == '__main__':
    r = 4
    h = 12
    result = calculate_cone_volume(r, h)
    print(result)