import numpy as np

def calculate_bounding_box_area(points):
    """
    Calculates the area of the smallest bounding box enclosing all points in a list of (x, y) tuples.
    
    Parameters:
        points (list[tuple]): A list of coordinate pairs [tuple], each tuple containing x and y coordinates.
        
    Returns:
        float: The area of the bounding box defined by min/max X and Y values. Raises ValueError if input is empty or invalid.
    """
    
    # Validate that at least one point exists
    if not points:
        raise ValueError("Input list 'points' must contain at least one coordinate tuple.")

    try:
        x_coords = [p[0] for p in points]
        y_coords = [p[1] for p in points]
        
        # Convert to numpy arrays for efficient vectorized operations
        xs = np.array(x_coords)
        ys = np.array(y_coords)

        min_x, max_x = np.min(xs), np.max(xs)
        min_y, max_y = np.min(ys), np.max(ys)
        
    except IndexError:
        raise ValueError("Each coordinate tuple must contain exactly two elements (x and y).")
    
    # Calculate width and height. If either is zero, the area will be zero if valid dimensions are 0-width or 0-height points overlap fully in one dimension but differ in another OR they share same position entirely -> return 0.0
        width = max_x - min_x 
        height = max_y - min_y
    
    # Return calculated area: product of width and height, handling zero dimensions gracefully if needed (though logically valid only if points coincide on at least one axis)
    
    area = np.abs(width * height)

    return float(area)

if __name__ == '__main__':
    sample_points = [(-1.0, -2.5), (3.0, 4.0), (-2.5, 6.7)]
    result_area = calculate_bounding_box_area(sample_points)

    print("Bounding Box Area:", result_area)