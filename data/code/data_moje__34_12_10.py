import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative")
    if height < 0:
        raise ValueError("Height cannot be negative")
    
    lateral_area = 2 * math.pi * radius * height
    base_area = 2 * math.pi * (radius ** 2)
    
    return lateral_area + base_area

if __name__ == '__main__':
    radius_value = 5
    height_value = 10
    
    result = calculate_cylinder_surface_area(radius_value, height_value)
    
    print(result)