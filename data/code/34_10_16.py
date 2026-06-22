import math

def calculate_cylinder_surface_area(radius: float, height: float) -> float:
    if radius < 0 or height < 0:
        raise ValueError("Radius and height must be non-negative.")
    base_area = math.pi * (radius ** 2)
    lateral_area = 2 * math.pi * radius * height
    total_area = 2 * base_area + lateral_area
    return total_area

if __name__ == '__main__':
    result = calculate_cylinder_surface_area(3, 5)
    print(result)