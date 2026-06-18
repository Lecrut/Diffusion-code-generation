import numpy as np

def calculate_smallest_bounding_box_area(coordinates):
    """
    Calculates the area of the smallest bounding box enclosing all given points.
    
    Parameters:
        coordinates (list or list-like of tuples/lists): List of (x, y) coordinate pairs.
        
    Returns:
        float: Area of the minimum-area rectangle that encloses all points.
               Assumes axis-aligned bounding box for simplicity unless otherwise specified;
               this implementation uses an axis-aligned approach as it's standard without 
               further geometric constraints specified. If a rotated box is required, 
               additional logic would be needed (e.g., convex hull + rotation).
    """
    if not coordinates:
        return 0.0

    # Convert list of tuples to numpy array for vector operations
    points = np.array(coordinates)
    
    # Extract x and y columns
    xs, ys = points[:, 0], points[:, 1]
    
    # Compute min/max along each axis
    xmin, xmax = xs.min(), xs.max()
    ymin, ymax = ys.min(), ys.max()
    
    width = xmax - xmin
    height = ymax - ymin
    
    area = width * height
    return float(area)

if __name__ == '__main__':
    # Hard-coded sample values (no user input required)
    sample_points = [
        (1, 2),
        (3, 4),
        (5, 6),
        (0, 0)
    ]

    area_result = calculate_smallest_bounding_box_area(sample_points)
    print(f"Area of the smallest bounding box: {area_result}")