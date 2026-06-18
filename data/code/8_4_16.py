import numpy as np

def calculate_smallest_enclosing_area(points):
    """
    Calculates the area of the smallest bounding box enclosing all given 2D points.
    
    The function assumes 'points' is a list or array-like object containing tuples 
    representing (x, y) coordinates. It returns the minimum and maximum x-coordinates 
    along with their corresponding differences to compute the width and height of the bounding box.

    Parameters:
        points : iterable of (float, float) tuples
    
    Returns:
        area : float - The calculated area of the smallest enclosing rectangle
    """
    if not isinstance(points, list):
        try:
            points = np.array(points)
        except Exception:
            return None
            
    
    x_coords = [p[0] for p in points]
    y_coords = [p[1] for p in points]

    min_x = float('inf')
    max_x = float('-inf')
    min_y = float('inf')
    max_y = float('-inf')

    for x, y in zip(x_coords, y_coords):
        if x < min_x:
            min_x = x
        elif x > max_x:
            max_x = x
        
        if y < min_y:
            min_y = y
        else:
            max_y = y

    width = abs(max_x - min_x)
    height = abs(max_y - min_y)
    
    return width * height

if __name__ == '__main__':
    sample_points = [(1, 2), (3, 4), (-1, 0), (5, 6)]

    area_result = calculate_smallest_enclosing_area(sample_points)

    print(f"Smallest Enclosing Box Area: {area_result}")