import math

def compute_cylinder_surface_area(radius, height):
    pi_squared_radius = math.pi * radius * radius
    circumference = 2 * math.pi * radius
    area_base = pi_squared_radius
    area_lateral = circumference * height
    total_surface_area = 2 * area_base + area_lateral
    return total_surface_area

if __name__ == '__main__':
    r = 7.5
    h = 12.0
    surface_area = compute_cylinder_surface_area(r, h)
    print(surface_area)