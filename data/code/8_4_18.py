import numpy as np

def calculate_bounding_box_area(coordinates: list[tuple[float | int, float | int]]) -> float:
    """
    Calculates the area of the smallest bounding box enclosing all given points.
    
    Args:
        coordinates (list): A list of tuples where each tuple represents a point (x, y).
        
    Returns:
        float: The area of the minimal bounding box that encloses all points.
               If fewer than 2 unique points exist or input is invalid, returns -1.0.
    """
    if not coordinates:
        return -1.0
    
    # Convert list to numpy array for efficient vector operations
    coords_array = np.array(coordinates)
    
    # Check minimum dimension requirement (at least one x and y per point)
    if len(coords_array.shape[1]) < 2:
        return -1.0
        
    try:
        xs = coords_array[:, 0]
        ys = coords_array[:, 1]
        
        min_x, max_x = np.min(xs), np.max(xs)
        min_y, max_y = np.min(ys), np.max(ys)
        
        width = abs(max_x - min_x)
        height = abs(max_y - min_y)
        
        area = width * height
        
        # Return 0.0 if all points are identical (degenerate case)
        return float(area)
    except Exception:
        return -1.0

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    sample_points_2d = [
        (1, 2),
        (3, 4),
        (-1, 5)
    ]

    result_area = calculate_bounding_box_area(sample_points_2d)
    
    print(f"Input points: {sample_points_2d}")
    print(f"Calculated bounding box area: {result_area}")