import math

def cylinder_surface_areas(radii, heights):
    radii = [float(r) for r in radii]
    heights = [float(h) for h in heights]
    areas = []
    for r, h in zip(radii, heights):
        if r < 0:
            r = -r
        if h < 0:
            h = -h
        area = 2 * math.pi * r * (r + h)
        areas.append(area)
    return areas

if __name__ == '__main__':
    radii = [1.0, 2.0, 3.0]
    heights = [2.0, 4.0, 6.0]
    result = cylinder_surface_areas(radii, heights)
    print(result)