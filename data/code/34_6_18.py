import math
import numpy as np

def calculate_cylinder_surface_areas(radii: np.ndarray, heights: np.ndarray) -> np.ndarray:
    radii = np.asarray(radii, dtype=np.float64)
    heights = np.asarray(heights, dtype=np.float64)
    
    r = radii.flatten()
    h = heights.flatten()
    
    areas = 2.0 * np.pi * r * (r + h)
    
    return areas

if __name__ == '__main__':
    radii_values = np.array([1.0, 2.0, 3.0])
    heights_values = np.array([1.0, 2.0, 3.0])
    
    results = calculate_cylinder_surface_areas(radii_values, heights_values)
    
    print(results)