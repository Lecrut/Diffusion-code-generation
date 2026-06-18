import numpy as np

def calculate_minimal_bounding_box_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all given coordinates.
    
    Parameters:
        coordinates (list or array-like): List of tuples representing (x, y) points.
        
    Returns:
        float: The area of the minimal bounding box.
    """
    # Convert input to numpy array for efficient vector operations
    coords_array = np.array(coordinates)
    
    if len(coords_array.shape) == 1 and coords_array.size > 0:
        # Handle case where a single tuple might be passed as list instead of nested list
        x_coords, y_coords = zip(*coords_array)
        points_2d = np.column_stack((x_coords, y_coords))
    else:
        points_2d = coords_array
    
    if len(points_2d.shape) == 0 or (len(points_2d.shape) == 1 and points_2d.size < 2):
        return 0.0

    # Extract x and y coordinates as column vectors for clarity, though row-wise is fine too here
    xs = points_2d[:, 0]
    ys = points_2d[:, 1]

    min_x = np.min(xs)
    max_x = np.max(xs)
    min_y = np.min(ys)
    max_y = np.max(ys)

    width = max_x - min_x
    height = max_y - min_y
    
    # Area is zero if any dimension has no extent (single point or duplicate points only in one axis)
    area = width * height

    return float(area)

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    sample_points_1 = [(0, 0), (2, 3)]
    
    sample_points_2 = [(-5.0, -4.0), (-1.0, 2.0), (6.0, 8.0)]

    # Test case 1: Simple rectangle
    area1 = calculate_minimal_bounding_box_area(sample_points_1)
    
    # Test case 2: Larger set of points forming a bounding box with some slack inside
    area2 = calculate_minimal_bounding_box_area(sample_points_2)

    print(f"Area for sample 1 (points {sample_points_1}): {area1}")
    print(f"Area for sample 2 (points {sample_points_2}): {area2}")
    
    # Additional test with single point to ensure robustness
    single_point = [(5, 5)]
    area_single = calculate_minimal_bounding_box_area(single_point)
    print(f"Area for single point: {area_single}")

    # Test with duplicate points
    duplicates = [(1, 2), (1, 2), (3, 4)]
    area_dup = calculate_minimal_bounding_box_area(duplicates)
    print(f"Area for points with duplicates ({duplicates}): {area_dup}")