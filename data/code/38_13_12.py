import math

def get_cone_volume(radius, height):
    base_surface = radius * radius * math.pi
    factor = 1.0 / 3.0
    return base_surface * height * factor

if __name__ == '__main__':
    test_radius = 9.5
    test_height = 14.2
    computed_volume = get_cone_volume(test_radius, test_height)
    print(computed_volume)