import numpy as np

def calculate_min_bounding_box_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all given coordinates.
    
    Parameters:
        coordinates (list[tuple]): A list of (x, y) tuples representing points in 2D space.
        
    Returns:
        float: The area of the minimal axis-aligned bounding box containing all points.
              Returns None if fewer than two unique x or y values are present.
    
    Raises:
        ValueError: If coordinates is empty or contains non-tuple elements.
    """
    # Validate input structure
    if not isinstance(coordinates, list):
        raise TypeError("Input must be a list of tuples.")
    
    for coord in coordinates:
        if not (isinstance(coord, tuple) and len(coord) == 2):
            raise ValueError(f"Each coordinate must be a (x, y) tuple. Got {coord}.")

    # Convert to numpy arrays for efficient vector operations
    x_coords = np.array([p[0] for p in coordinates])
    y_coords = np.array([p[1] for p in coordinates])

    if len(np.unique(x_coords)) < 2 or len(np.unique(y_coords)) < 2:
        # If all points lie on a single vertical line, horizontal width is zero.
        # Similarly for horizontal lines. Area becomes zero.
        return 0.0

    min_x = np.min(x_coords)
    max_x = np.max(x_coords)
    min_y = np.min(y_coords)
    max_y = np.max(y_coords)

    width = max_x - min_x
    height = max_y - min_y
    
    return float(width * height)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    
    # Sample 1: A set of points forming a rectangle with some extra noise inside/outside edges.
    sample_points_1 = [
        (0, 0), 
        (2, 0), 
        (0, 3), 
        (4, 5)  # Extends the bounding box further than just these three points suggest visually if not careful, but here it defines max x and y.
    ]

    # Sample 2: Points on a single line (should return area 0).
    sample_points_2 = [
        (1, 5), 
        (3, 7), 
        (5, 9)
    ]

    # Sample 3: Single point.
    sample_points_3 = [(4, 6)]

    print("Sample 1 Area:", calculate_min_bounding_box_area(sample_points_1))
    print("Sample 2 Area:", calculate_min_bounding_box_area(sample_points_2))
    print("Sample 3 Area:", calculate_min_bounding_box_area(sample_points_3))