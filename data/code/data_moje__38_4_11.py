import math

def compute_base_area(radius):
    return math.pi * radius * radius

def compute_cone_volume(base_area, height):
    return base_area * height / 3

def calculate_cone_volume(radius, height):
    base_area = compute_base_area(radius)
    return compute_cone_volume(base_area, height)

if __name__ == '__main__':
    sample_radius = 6
    sample_height = 9
    final_volume = calculate_cone_volume(sample_radius, sample_height)
    print(final_volume)