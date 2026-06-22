import numpy as np

def calculate_cylinder_surface_area(radii, heights):
    radii_array = np.asarray(radii, dtype=np.float64)
    heights_array = np.asarray(heights, dtype=np.float64)
    if radii_array.shape != heights_array.shape:
        raise ValueError("Radii and heights arrays must have the same shape")
    if np.any(radii_array < 0) or np.any(heights_array < 0):
        raise ValueError("Radii and heights must be non-negative")
    lateral_area = 2 * np.pi * radii_array * heights_array
    base_area = 2 * np.pi * np.square(radii_array)
    total_area = lateral_area + base_area
    return total_area

if __name__ == '__main__':
    sample_radii = np.array([1.0, 2.0, 5.0, 0.0])
    sample_heights = np.array([3.0, 4.0, 10.0, 5.0])
    result = calculate_cylinder_surface_area(sample_radii, sample_heights)
    print(result)