import math

def cylinder_surface_area(radii, heights):
    radii_list = [float(r) for r in radii]
    heights_list = [float(h) for h in heights]
    
    if len(radii_list) != len(heights_list):
        raise ValueError("Radii and heights arrays must have the same length.")
    
    if len(radii_list) == 0:
        return []
    
    areas = []
    for r, h in zip(radii_list, heights_list):
        if r < 0:
            raise ValueError("Radius cannot be negative.")
        if h < 0:
            raise ValueError("Height cannot be negative.")
        
        lateral_area = 2 * math.pi * r * h
        base_area = 2 * math.pi * r * r
        total_area = lateral_area + base_area
        areas.append(total_area)
    
    return areas

if __name__ == '__main__':
    radii = [1.0, 2.0, 3.0]
    heights = [5.0, 4.0, 3.0]
    result = cylinder_surface_area(radii, heights)
    print(result)