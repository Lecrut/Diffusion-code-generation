import numpy as np

def calculate_cylinder_surface_area(radii, heights):
    radii = np.asarray(radii, dtype=np.float64)
    heights = np.asarray(heights, dtype=np.float64)
    two_pi = 2.0 * np.pi
    base_area = two_pi * radii * radii
    lateral_area = two_pi * radii * heights
    return base_area + lateral_area

if __name__ == '__main__':
    sample_radii = np.array([1.0, 2.5, 0.0, 10.0])
    sample_heights = np.array([5.0, 3.0, 4.0, 2.0])
    result = calculate_cylinder_surface_area(sample_radii, sample_heights)
    print(result)