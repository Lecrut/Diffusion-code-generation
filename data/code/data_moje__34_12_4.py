import math

def cylinder_surface_area(radius, height):
    if radius < 0 or height < 0:
        raise ValueError("Dimensions must be non-negative.")
    
    lateral_area = 2 * math.pi * radius * height
    base_areas = 2 * math.pi * (radius ** 2)
    
    return lateral_area + base_areas

if __name__ == '__main__':
    radius = 5
    height = 10
    area = cylinder_surface_area(radius, height)
    print(area)