import math

def calculate_cylinder_surface_area(radius, height):
    if radius <= 0 or height <= 0:
        raise ValueError("Radius and height must be positive.")
    
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * (radius ** 2)
    total_surface_area = lateral_area + base_area
    return total_surface_area

if __name__ == '__main__':
    radius = 5.0
    height = 10.0
    result = calculate_cylinder_surface_area(radius, height)
    print(result)