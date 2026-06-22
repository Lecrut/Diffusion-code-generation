import numpy as np

def calculate_cylinder_surface_area(radii, heights):
    radii_arr = np.asarray(radii, dtype=np.float64)
    heights_arr = np.asarray(heights, dtype=np.float64)
    return 2 * np.pi * radii_arr * (radii_arr + heights_arr)

if __name__ == '__main__':
    sample_radii = np.array([1.0, 2.0, 5.5])
    sample_heights = np.array([3.0, 4.0, 10.0])
    result = calculate_cylinder_surface_area(sample_radii, sample_heights)
    print(result)