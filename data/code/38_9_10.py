import math

def calculate_cone_volume(radius, height):
    if radius <= 0:
        raise ValueError("Radius must be positive.")
    if height <= 0:
        raise ValueError("Height must be positive.")
    base_area = math.pi * (radius ** 2)
    volume = base_area * height / 3.0
    return volume

if __name__ == '__main__':
    sample_radius = 10
    sample_height = 20
    computed_volume = calculate_cone_volume(sample_radius, sample_height)
    print(computed_volume)