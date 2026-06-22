import math

def cylinder_surface_area(radii, heights):
    return [2 * math.pi * r * (r + h) for r, h in zip(radii, heights)]
if __name__ == '__main__':
    radii = [1.0, 2.0, 3.0, 4.0, 5.0]
    heights = [2.0, 3.0, 4.0, 5.0, 6.0]
    surface_areas = cylinder_surface_area(radii, heights)
    print(surface_areas)