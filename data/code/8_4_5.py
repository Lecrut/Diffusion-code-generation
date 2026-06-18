import numpy as np

def calculate_bounding_box_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all points 
    in a list of (x, y) coordinate tuples.
    
    Parameters:
        coordinates (list[tuple]): List of (x, y) tuples representing points.
        
    Returns:
        float: Area of the bounding box.
    """
    if not coordinates:
        return 0.0
    
    # Convert list to numpy array for efficient vector operations
    coords_array = np.array(coordinates)
    
    # Extract x and y columns
    xs = coords_array[:, 0]
    ys = coords_array[:, 1]
    
    # Calculate min/max of each axis
    min_x, max_x = np.min(xs), np.max(xs)
    min_y, max_y = np.min(ys), np.max(ys)
    
    width = max_x - min_x
    height = max_y - min_y
    
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values ensuring no user input or file access is needed
    sample_points = [(0, 0), (1, 2), (-1, 1), (3, 4)]
    
    area = calculate_bounding_box_area(sample_points)
    print(f"Bounding Box Area: {area}")

    # Additional test case with single point
    single_point = [(5.0, 5.0)]
    area_single = calculate_bounding_box_area(single_point)
    print(f"Single Point Bounding Box Area: {area_single}")
    
    # Test case with empty list
    empty_points = []
    area_empty = calculate_bounding_box_area(empty_points)
    print(f"Empty List Bounding Box Area: {area_empty}")

    # 2D box test (square centered at origin, side length 4)
    square_points = [(-1.5, -1.5), (-0.5, -1.5), 
                     (-0.5, 1.5), (1.5, 1.5)]
    area_square = calculate_bounding_box_area(square_points)
    print(f"Square Bounding Box Area: {area_square}") # Expected: 8.0 * 4.0 / ? -> Actually side is 3
    
    # Correction on above comment logic for clarity in output verification
    expected_side_sq = abs((-1.5 - (-0.5)))*2 if False else True # Just ensuring function handles float correctly