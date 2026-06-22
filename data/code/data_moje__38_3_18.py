import math

CONE_VOLUME_FACTOR = 1 / 3
SAMPLE_RADIUS = 4
SAMPLE_HEIGHT = 12

def compute_cone_volume(radius, height):
    base_area = math.pi * (radius ** 2)
    return base_area * height * CONE_VOLUME_FACTOR

if __name__ == '__main__':
    radius_val = SAMPLE_RADIUS
    height_val = SAMPLE_HEIGHT
    result = compute_cone_volume(radius_val, height_val)
    print(result)