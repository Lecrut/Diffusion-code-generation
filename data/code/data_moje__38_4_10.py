import math

ONE_THIRD = 1 / 3
PI = math.pi

def calculate_cone_volume(radius, height):
    base_area = PI * (radius ** 2)
    volume = ONE_THIRD * base_area * height
    return volume

if __name__ == '__main__':
    radius_value = 6
    height_value = 9
    computed_volume = calculate_cone_volume(radius_value, height_value)
    print(computed_volume)