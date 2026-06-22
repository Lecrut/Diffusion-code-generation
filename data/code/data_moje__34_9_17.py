import math

def cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative")
    base_area = math.pi * radius ** 2
    side_area = 2 * math.pi * radius * height
    return 2 * base_area + side_area

if __name__ == "__main__":
    sample_radius = 3.0
    sample_height = 7.0
    area = cylinder_surface_area(sample_radius, sample_height)
    print(area)