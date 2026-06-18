import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple]): A list of (x, y) tuples representing the coordinates 
                                of the polygon's vertices in order (clockwise or counter-clockwise).
                                
    Returns:
        float: The area of the polygon as a non-negative value.
        
    Raises:
        ValueError: If fewer than 3 unique vertices are provided.
    """
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least 3 vertices.")
    
    n = len(vertices)
    sum1 = 0.0
    sum2 = 0.0
    
    for i in range(n):
        x_i, y_i = vertices[i]
        x_next, y_next = vertices[(i + 1) % n]
        
        sum1 += x_i * y_next
        sum2 += y_i * x_next
        
    area = abs(sum1 - sum2) / 2.0
    
    return area

if __name__ == '__main__':
    # Sample polygon vertices: a rectangle with corners at (0,0), (4,0), (4,3), (0,3)
    sample_vertices = [(0, 0), (4, 0), (4, 3), (0, 3)]
    
    area = calculate_polygon_area(sample_vertices)
    print(f"The calculated area of the polygon is: {area}")

    # Another test case with a triangle: vertices at (-1,-2), (9,2), (-5,-4)
    sample_triangle = [(-1, -2), (9, 2), (-5, -4)]
    tri_area = calculate_polygon_area(sample_triangle)
    print(f"The calculated area of the test triangle is: {tri_area}")

    # Test with invalid input (less than 3 vertices) should raise an error
    try:
        calculate_polygon_area([(0, 1), (2, 3)])
    except ValueError as e:
        print(f"Error caught for insufficient vertices: {e}")