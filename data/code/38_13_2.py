import math

def compute_cone_volume(radius, height):
    base_area = math.pi * radius * radius
    volume = (base_area * height) / 3
    return volume

if __name__ == '__main__':
    sample_radius = 7.5
    sample_height = 12.0
    calculated_volume = compute_cone_volume(sample_radius, sample_height)
    print(calculated_volume)