import math

def calculate_cylinder_surface_area():
    radius = 5.0
    height = 10.0
    
    lateral_area = 2 * math.pi * radius * height
    base_area = math.pi * radius ** 2
    total_area = lateral_area + 2 * base_area
    
    return {
        "lateral_surface_area": lateral_area,
        "total_surface_area": total_area
    }

if __name__ == '__main__':
    result = calculate_cylinder_surface_area()
    print(result["lateral_surface_area"])
    print(result["total_surface_area"])