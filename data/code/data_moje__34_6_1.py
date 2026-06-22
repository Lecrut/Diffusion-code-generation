import math
import numpy as np

def cylinder_surface_area(radii, heights):
    radii_arr = np.asarray(radii, dtype=np.float64)
    heights_arr = np.asarray(heights, dtype=np.float64)
    r = np.abs(radii_arr)
    h = np.abs(heights_arr)
    lateral = 2.0 * np.pi * r * h
    bases = 2.0 * np.pi * (r ** 2)
    total = lateral + bases
    return total

if __name__ == '__main__':
    radii_values = [3.0, 5.0, 0.0, 1.0]
    heights_values = [10.0, 2.0, 5.0, 4.0]
    results = cylinder_surface_area(radii_values, heights_values)
    print(results)