import math

def get_cylinder_surface_area(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Dimensions must be positive")
    top_bottom_area = 2 * math.pi * radius ** 2
    side_area = 2 * math.pi * radius * height
    return top_bottom_area + side_area

if __name__ == '__main__':
    sample_radius = 3.5
    sample_height = 7.0
    area = get_cylinder_surface_area(sample_radius, sample_height)
    print(area)