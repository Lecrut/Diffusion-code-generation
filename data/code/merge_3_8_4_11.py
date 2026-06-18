import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all points in a list of coordinates.
    
    Parameters:
        coordinates (list[tuple]): A list of tuples where each tuple represents an (x, y) coordinate pair.
        
    Returns:
        float: The area of the smallest bounding box that encloses all given points.
              If fewer than 2 unique x or y values exist, returns 0.0.
    
    Raises:
        ValueError: If coordinates is empty or not a list/tuple of tuples.
    """
    if not isinstance(coordinates, (list, tuple)) or len(coordinates) == 0:
        raise ValueError("Input must be a non-empty list or tuple of coordinate tuples.")

    # Convert to numpy array for efficient vector operations
    points_array = np.array([coord[:2] for coord in coordinates], dtype=float)
    
    if points_array.ndim != 2 or points_array.shape[1] != 2:
        raise ValueError("Each element must be a tuple of two values (x, y).")

    # Calculate min and max x and y separately to find the bounding box dimensions
    width = np.max(points_array[:, 0]) - np.min(points_array[:, 0])
    height = np.max(points_array[:, 1]) - np.min(points_array[:, 1])

    if width <= 0 or height <= 0:
        return 0.0
    
    area = width * height
    return float(area)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no files, no network access)
    sample_coordinates = [
        (1.5, 2.3),
        (4.0, 6.7),
        (2.1, 8.9),
        (-1.2, -3.4),
        (0.0, 0.0)
    ]

    area = calculate_smallest_bounding_box_area(sample_coordinates)
    
    print(f"Input coordinates: {sample_coordinates}")
    print(f"Smallest bounding box area: {area:.4f} square units")