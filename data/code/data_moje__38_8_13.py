import math

CONE_VOLUME_DIVISOR = 3

def calculate_cone_volume(radius, height):
    base_area = math.pi * radius * radius
    volume = base_area * height / CONE_VOLUME_DIVISOR
    return volume

if __name__ == '__main__':
    target_radius = 8
    target_height = 11
    computed_volume = calculate_cone_volume(target_radius, target_height)
    print(f"{computed_volume:.2f}")