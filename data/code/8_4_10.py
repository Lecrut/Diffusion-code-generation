import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all given points.
    
    Parameters:
        coordinates (list or array-like): A list of tuples representing (x, y) coordinates.
        
    Returns:
        float: The area of the minimal axis-aligned bounding box.
    """
    # Convert input to numpy array for vectorized operations
    coords_array = np.array(coordinates)
    
    if len(coords_array) == 0:
        return 0.0
    
    # Extract x and y coordinates as separate arrays
    xs = coords_array[:, 0]
    ys = coords_array[:, 1]
    
    # Calculate the range for each dimension (width and height)
    width = np.max(xs) - np.min(xs)
    height = np.max(ys) - np.min(ys)
    
    # Area is simply width * height
    area = width * height
    
    return float(area)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input or files needed)
    sample_points = [
        (1.0, 2.0),
        (3.5, 4.0),
        (2.0, 6.0),
        (4.0, 1.0)
    ]

    # Calculate the area of the bounding box enclosing these points
    result_area = calculate_smallest_bounding_box_area(sample_points)

    print(f"Sample coordinates: {sample_points}")
    print(f"Smallest bounding box area: {result_area}")