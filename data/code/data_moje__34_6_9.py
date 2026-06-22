import numpy as np

def calculate_cylinder_surface_area(radii, heights):
    radii_array = np.asarray(radii, dtype=np.float64)
    heights_array = np.asarray(heights, dtype=np.float64)
    
    if radii_array.shape != heights_array.shape:
        raise ValueError("Radii and heights arrays must have the same shape")
    
    if np.any(radii_array < 0) or np.any(heights_array < 0):
        raise ValueError("Radii and heights must be non-negative")
    
    if np.any(np.isinf(radii_array)) or np.any(np.isinf(heights_array)):
        raise ValueError("Radii and heights must not be infinite")
    
    side_area = 2.0 * np.pi * radii_array * heights_array
    top_bottom_area = 2.0 * np.pi * radii_array ** 2
    
    total_area = side_area + top_bottom_area
    return total_area

if __name__ == '__main__':
    test_radii = np.array([1.0, 2.5, 5.0])
    test_heights = np.array([10.0, 4.0, 2.0])
    result = calculate_cylinder_surface_area(test_radii, test_heights)
    print(result)