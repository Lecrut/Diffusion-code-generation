import numpy as np

def calculate_min_bounding_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all given (x, y) coordinates.

    Args:
        coordinates (list[tuple]): A list of tuples containing x and y coordinates.

    Returns:
        float: The area of the minimum bounding rectangle that encloses all points.
              If no points are provided or input is invalid, returns 0.0.
    """
    if not isinstance(coordinates, list) or len(coordinates) == 0:
        return 0.0

    try:
        # Convert list of tuples to a numpy array for vectorized operations
        x_coords = np.array([coord[0] for coord in coordinates])
        y_coords = np.array([coord[1] for coord in coordinates])

        if len(x_coords) == 0 or len(y_coords) == 0:
            return 0.0

        # Calculate width and height of the bounding box by finding min/max differences
        width = float(np.max(x_coords)) - float(np.min(x_coords))
        height = float(np.max(y_coords)) - float(np.min(y_coords))

        area = width * height
        return float(area) if not np.isnan(width) or not np.isnan(height) else 0.0
        
    except (TypeError, ValueError):
        # Return 0 for invalid coordinate types
        return 0.0

if __name__ == '__main__':
    # Hard-coded sample values as per task requirements
    sample_points = [
        (1.5, 2.3),
        (4.2, 6.7),
        (-0.8, -1.2),
        (3.9, 4.5)
    ]

    area_result = calculate_min_bounding_area(sample_points)

    print(f"Input coordinates: {sample_points}")
    print(f"Smallest bounding box area: {area_result:.6f}")

    # Additional test case with duplicate points (zero width/height if all same)
    sample_duplicates = [
        (5.0, 10.0),
        (5.0, 10.0),
        (7.0, 8.0)
    ]

    area_result_dup = calculate_min_bounding_area(sample_duplicates)

    print(f"Input coordinates with duplicates: {sample_duplicates}")
    print(f"Bounding box area for duplicate case: {area_result_dup:.6f}")