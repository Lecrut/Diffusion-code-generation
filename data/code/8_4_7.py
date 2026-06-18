import numpy as np

def min_bounding_box_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all points 
    in a list of (x, y) coordinates.
    
    Parameters:
        coordinates (list[tuple]): List of tuples where each tuple is an (x, y) coordinate pair.
        
    Returns:
        float: The area of the minimum bounding box enclosing all points.
              If fewer than two unique dimensions exist or list is empty, returns 0.0.
    """
    if len(coordinates) < 2:
        return 0.0
    
    # Convert list to numpy array for efficient vector operations
    coords_array = np.array(coordinates, dtype=float).T
    
    # Calculate width and height as range between min and max coordinates per axis
    x_coords = coords_array[:, 0]
    y_coords = coords_array[:, 1]

    try:
        return (np.max(x_coords) - np.min(x_coords)) * (np.max(y_coords) - np.min(y_coords))
    except ValueError:
        # Handle cases where min/max might fail on degenerate data if any, though unlikely here
        return 0.0

if __name__ == '__main__':
    sample_points = [
        (1.5, 2.3),
        (4.8, 6.7),
        (3.2, -1.5),
        (-2.1, 9.8),
        (0.0, 0.0)
    ]
    
    area = min_bounding_box_area(sample_points)
    print(f"Minimum bounding box enclosing all sample points has an area of: {area:.4f}")