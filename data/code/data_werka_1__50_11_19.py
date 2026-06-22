import numpy as np

def validate_raster_grid(grid):
    if not isinstance(grid, np.ndarray) or grid.dtype != bool:
        raise ValueError('Input must be a boolean NumPy array.')

def calculate_area_difference(raster1, raster2):
    validate_raster_grid(raster1)
    validate_raster_grid(raster2)
    area_diff = np.sum(np.bitwise_xor(raster1, raster2))
    return area_diff
if __name__ == '__main__':
    grid_a = np.array([[True, False, True], [False, True, False]], dtype=bool)
    grid_b = np.array([[True, True, False], [False, False, True]], dtype=bool)
    result1 = calculate_area_difference(grid_a, grid_b)
    print(result1)
    grid_c = np.array([[True, True, True], [True, True, True]], dtype=bool)
    grid_d = np.array([[False, False, False], [False, False, False]], dtype=bool)
    result2 = calculate_area_difference(grid_c, grid_d)
    print(result2)
    grid_e = np.array([[True, False, True], [False, True, False]], dtype=bool)
    grid_f = np.array([[True, False, True], [False, True, False]], dtype=bool)
    result3 = calculate_area_difference(grid_e, grid_f)
    print(result3)