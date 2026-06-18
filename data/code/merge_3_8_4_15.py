import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all given coordinates.
    
    Parameters:
        coordinates (list or array-like): List of tuples representing (x, y) points.
        
    Returns:
        float: Area of the minimal axis-aligned bounding box.
    """
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list.")
    
    if len(coordinates) == 0:
        return 0.0

    # Convert to numpy array for efficient vector operations
    points_array = np.array(coordinates)
    
    # Extract x and y coordinates as separate arrays
    xs, ys = points_array[:, 0], points_array[:, 1]
    
    # Calculate the range (width and height) of the bounding box
    width = float(np.max(xs)) - float(np.min(xs))
    height = float(np.max(ys)) - float(np.min(ys))
    
    return width * height

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    sample_points = [
        (1, 2),
        (3, 4),
        (5, 6),
        (0, 8)
    ]

    area = calculate_smallest_bounding_box_area(sample_points)
    
    print(f"Coordinates: {sample_points}")
    print(f"Smallest bounding box area: {area}")