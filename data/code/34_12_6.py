import math

def calculate_cylinder_surface_area(radius, height):
    if radius < 0:
        raise ValueError("Radius cannot be negative.")
    if height < 0:
        raise ValueError("Height cannot be negative.")
    
    area = 2 * math.pi * radius * (radius + height)
    return area

if __name__ == '__main__':
    result = calculate_cylinder_surface_area(3, 5)
    print(result)