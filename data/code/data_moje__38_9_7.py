import math

def compute_base_area(radius):
    return math.pi * radius * radius

def calculate_cone_volume(radius, height):
    base_area = compute_base_area(radius)
    fraction = 1 / 3
    volume = fraction * base_area * height
    return volume

if __name__ == '__main__':
    sample_radius = 10
    sample_height = 20
    result = calculate_cone_volume(sample_radius, sample_height)
    print(result)