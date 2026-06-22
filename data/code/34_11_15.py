import math

def compute_cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError('Radius and height must be non-negative')
    base_area = math.pi * radius ** 2
    lateral_surface_area = 2 * math.pi * radius * height
    total_surface_area = 2 * base_area + lateral_surface_area
    return (lateral_surface_area, total_surface_area)
if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    lateral_area, total_area = compute_cylinder_surface_area(radius, height)
    print(lateral_area)
    print(total_area)