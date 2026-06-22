import math
import numpy as np

def cylinder_surface_area(radii, heights):
    radii = np.asarray(radii, dtype=np.float64)
    heights = np.asarray(heights, dtype=np.float64)
    
    if radii.size == 0 or heights.size == 0:
        return np.array([])
    
    if np.any(radii < 0) or np.any(heights < 0):
        raise ValueError("Radii and heights must be non-negative")
    
    r_sq = radii ** 2
    two_pi_r_h = 2.0 * math.pi * radii * heights
    two_pi_r_sq = 2.0 * math.pi * r_sq
    
    area = two_pi_r_h + two_pi_r_sq
    
    return area

if __name__ == '__main__':
    r_vals = [1.0, 2.0, 0.0]
    h_vals = [2.0, 3.0, 5.0]
    
    result = cylinder_surface_area(r_vals, h_vals)
    print(result)