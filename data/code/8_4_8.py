import numpy as np

def calculate_minimal_bounding_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all given points.
    
    Parameters:
        coordinates (list of tuple or array-like): List of (x, y) coordinate tuples.
        
    Returns:
        float: Area of the minimal bounding rectangle enclosing the points.
               If no points are provided, returns 0.0.
    """
    if not isinstance(coordinates, list) or len(coordinates) == 0:
        return 0.0
    
    # Convert input to numpy array for efficient vector operations
    coords_array = np.array([coord[0] for coord in coordinates])
    y_coords_array = np.array([coord[1] for coord in coordinates])
    
    if len(coords_array) == 0 or len(y_coords_array) == 0:
        return 0.0
    
    # Calculate the range of x and y coordinates to determine bounding box dimensions
    width = float(np.max(coords_array)) - float(np.min(coords_array))
    height = float(np.max(y_coords_array)) - float(np.min(y_coords_array))
    
    area = width * height
    
    return area

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_points_1d = [(0, 0), (2, 3)]
    sample_points_2d = [(-5.0, -4.0), (-6.5, -9.0), (8.7, 2.1), (8.0, 5.0)]

    # Calculate areas for samples
    area_result_1 = calculate_minimal_bounding_area(sample_points_1d)
    print(f"Area of bounding box enclosing {sample_points_1d}: {area_result_1}")

    area_result_2 = calculate_minimal_bounding_area(sample_points_2d)
    print(f"Area of bounding box enclosing {sample_points_2d}: {area_result_2}")

    # Test edge case with empty list
    empty_list_area = calculate_minimal_bounding_area([])
    print(f"Area for empty input: {empty_list_area}")