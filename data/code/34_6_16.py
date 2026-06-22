import numpy as np

def calculate_cylinder_surface_area(radii, heights):
    radii = np.asarray(radii, dtype=float)
    heights = np.asarray(heights, dtype=float)
    safe_radii = np.where(radii >= 0, radii, np.finfo(float).eps)
    safe_heights = np.where(heights >= 0, heights, np.finfo(float).eps)
    base_area = 2.0 * np.pi * safe_radii * safe_radii
    lateral_area = 2.0 * np.pi * safe_radii * safe_heights
    return base_area + lateral_area

if __name__ == '__main__':
    radii_input = np.array([1.0, 2.5, 5.0, 0.0, 10.0])
    heights_input = np.array([1.0, 3.0, 2.5, 4.0, 15.0])
    result = calculate_cylinder_surface_area(radii_input, heights_input)
    print(result)