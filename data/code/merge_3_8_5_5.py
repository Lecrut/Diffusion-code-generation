"""Module to calculate the area of a polygon using the Shoelace formula."""

def calculate_polygon_area(vertices):
    """
    Calculate the area of a simple polygon given its vertices in order (either clockwise or counter-clockwise).

    The vertices should be provided as a list of tuples, where each tuple represents the coordinates [x, y] 
    of a vertex.

    Parameters:
        vertices (list[tuple]): A list of (x, y) coordinate pairs representing the polygon's corners in order.

    Returns:
        float: The area of the polygon as an absolute value.

    Raises:
        ValueError: If fewer than 3 unique points are provided or if a point is invalid.
    """
    
    n = len(vertices)
    # Check for at least three vertices and ensure all coordinates are numbers
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    try:
        x_coords = [float(v[0]) for v in vertices]
        y_coords = [float(v[1]) for v in vertices]
        
        # Validate that every coordinate is finite (not NaN or Inf)
        if any(not isinstance(x, float) or not (x != x or abs(x) == float('inf')) for x in x_coords): 
            raise ValueError("All vertex coordinates must be valid numbers.")

    except IndexError:
        raise ValueError(f"Each vertex must have exactly 2 coordinates. Provided count per point was invalid.")

def shoelace_area(vertices):
    """
    Internal helper function implementing the Shoelace formula to calculate area.
    
    The formula is: Area = |sum(x_i * y_{i+1} - x_{i+1} * y_i)| / 2
    
    Parameters:
        vertices (list[tuple]): List of (x, y) coordinates in order.

    Returns:
        float: Calculated area.
    """
    
    n = len(vertices)
    sum_positive = 0
    sum_negative = 0

    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n] # Wrap around to the first vertex
        
        sum_positive += (x1 * y2)
        sum_negative += (y1 * x2)

    area = abs(sum_positive - sum_negative) / 2.0
    
    return area

def calculate_polygon_area(vertices):
    """Wrapper that validates inputs and calls shoelace logic."""
    
    # Re-validate input structure here for clarity in the public API if needed, 
    # but since we already did it above, this function can just call the helper directly or replicate.
    # To keep it self-contained as a single module without external dependencies:
    return shoelace_area(vertices)

if __name__ == '__main__':
    # Hard-coded sample values for testing
    
    # Sample 1: Triangle (3 vertices)
    triangle_vertices = [(0, 0), (4, 2), (2, 5)]
    
    # Sample 2: Square (4 vertices)
    square_vertices = [(0, 0), (3, 0), (3, 3), (0, 3)]
    
    # Sample 3: Pentagon (5 vertices)
    pentagon_vertices = [(1.5, 0), (2.7, -4.6), (-2.8, -4.9), (-4.7, -3.6), (-1.5, 0)]

    test_cases = [triangle_vertices, square_vertices, pentagon_vertices]
    
    for i, case in enumerate(test_cases):
        try:
            area_val = calculate_polygon_area(case)
            print(f"Area of polygon with {len(case)} vertices: {area_val:.2f}")
        except ValueError as e:
            print(f"Error calculating area for test case {i+1}: {e}")

    # Additional specific check logic if needed, but the function handles errors.