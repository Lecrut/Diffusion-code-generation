import math

def calculate_cone_volume(radius, height):
    base_area = math.pi * radius ** 2
    one_third = 1 / 3
    volume = one_third * base_area * height
    return volume

if __name__ == '__main__':
    r = 10
    h = 20
    computed_volume = calculate_cone_volume(r, h)
    print(computed_volume)