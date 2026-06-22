import numpy as np

def calculate_cylinder_surface_area(radii, heights):
    radii = np.asarray(radii, dtype=np.float64)
    heights = np.asarray(heights, dtype=np.float64)
    
    if radii.shape != heights.shape:
        raise ValueError("radii and heights must have the same shape")
    
    if np.any(radii < 0) or np.any(heights < 0):
        raise ValueError("radii and heights must be non-negative")
    
    two_pi_r = 2 * np.pi * radii
    lateral_area = two_pi_r * heights
    base_area = np.pi * np.square(radii)
    total_area = lateral_area + 2 * base_area
    
    return total_area

if __name__ == '__main__':
    sample_radii = np.array([1.0, 2.5, 3.0])
    sample_heights = np.array([4.0, 5.0, 6.0])
    result = calculate_cylinder_surface_area(sample_radii, sample_heights)
    print(result)