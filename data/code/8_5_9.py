import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of [x, y] coordinates representing 
                                            ordered vertices of the polygon.
                                            
    Returns:
        float: The calculated area of the polygon. If fewer than 3 vertices are provided,
               returns 0.0.
    """
    n = len(vertices)
    
    if n < 3:
        return 0.0
    
    # Ensure vertices form a closed loop by appending the first vertex at the end
    extended_vertices = vertices + [vertices[0]]
    
    area = 0.5 * abs(sum(extended_vertices[i][0] * extended_vertices[(i+1) % n][1] - 
                         extended_vertices[i][1] * extended_vertices[(i+1) % n][0]) for i in range(n))
    
    return area

if __name__ == '__main__':
    # Hard-coded sample values representing a square with vertices (0,0), (4,0), (4,4), (0,4)
    square_vertices = [(0.0, 0.0), (4.0, 0.0), (4.0, 4.0), (0.0, 4.0)]
    
    # Another sample: a triangle with vertices (-1,-1), (2,3), (-5,1)
    triangle_vertices = [(-1.0, -1.0), (2.0, 3.0), (-5.0, 1.0)]
    
    print(f"Area of square: {calculate_polygon_area(square_vertices)}") # Expected output: 16.0
    print(f"Area of triangle: {calculate_polygon_area(triangle_vertices)}") # Expected output: 9.0
    
    # Sample with insufficient vertices (should return 0)
    invalid_vertices = [(1.0, 2.0)]
    print(f"Area of polygon with <3 vertices: {calculate_polygon_area(invalid_vertices)}") # Expected output: 0.0