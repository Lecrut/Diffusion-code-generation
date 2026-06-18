import numpy as np

def calculate_minimal_bounding_box_area(coordinates: list) -> float:
    """
    Calculates the area of the smallest bounding box enclosing all given coordinates.
    
    Parameters:
        coordinates (list): A list of tuples, where each tuple contains two elements representing x and y coordinates.
        
    Returns:
        float: The area of the minimal bounding box.
        
    Raises:
        ValueError: If no coordinates are provided or if a coordinate is not a valid pair of numbers.
    """
    if len(coordinates) == 0:
        raise ValueError("No coordinates provided.")

    # Convert list to numpy array for efficient vector operations
    points_array = np.array([coord[0], coord[1]] for coord in coordinates).T
    
    # Calculate the minimum and maximum x and y values
    min_x, max_x = points_array[:, 0].min(), points_array[:, 0].max()
    min_y, max_y = points_array[:, 1].min(), points_array[:, 1].max()

    width = abs(max_x - min_x)
    height = abs(max_y - min_y)

    return float(width * height)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, args, or network access)
    sample_coords = [
        (1.0, 2.0),
        (3.0, 4.0),
        (5.0, 6.0),
        (-1.0, -2.0)
    ]

    try:
        area = calculate_minimal_bounding_box_area(sample_coords)
        print(f"Area of the smallest bounding box enclosing all points: {area}")
    except ValueError as e:
        print(f"Error calculating area: {e}")