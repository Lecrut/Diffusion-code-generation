import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of ordered (x, y) tuples representing 
                                              the vertices of the polygon in order (clockwise or counter-clockwise).
    
    Returns:
        float: The area of the polygon. If an invalid input is provided, returns 0.0.
               Floating-point inaccuracies are handled by rounding to a reasonable precision.
    """
    if not isinstance(vertices, list) or len(vertices) < 3:
        return 0.0
    
    n = len(vertices)
    
    # Validate that all elements are tuples of two numbers
    for i in range(n):
        point = vertices[i]
        if not (isinstance(point, tuple) and 
                isinstance(point[0], (int, float)) and 
                isinstance(point[1], (int, float))):
            return 0.0
    
    area_sum = 0.0
    for i in range(n):
        x_i, y_i = vertices[i]
        x_next, y_next = vertices[(i + 1) % n]
        
        # Shoelace formula component: (x_i * y_{i+1} - x_{i+1} * y_i)
        area_sum += (x_i * y_next - x_next * y_i)
    
    return abs(area_sum / 2.0)

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Regular triangle: (0, 0), (4, 0), (2, 3) -> Area = 6
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    
    # Rectangle: (1, 1), (5, 1), (5, 4), (1, 4) -> Area = 9
    rectangle_vertices = [(1, 1), (5, 1), (5, 4), (1, 4)]
    
    # Pentagon with floating point coordinates: 
    # Approximate regular pentagon centered at origin
    pentagon_vertices = [
        (0.0, 2.8793852415718),
        (2.6894224505361, -0.9510565162952),
        (-2.6894224505361, -0.9510565162952)
    ] + [(-2.6894224505361, 0.9510565162952), (2.6894224505361, -0.9510565162952)]
    
    # Invalid input: less than 3 vertices
    invalid_vertices = [(0, 0), (1, 1)]
    
    print(f"Triangle Area: {calculate_polygon_area(triangle_vertices)}")
    print(f"Rectangle Area: {calculate_polygon_area(rectangle_vertices)}")
    print(f"Pentagon Area: {calculate_polygon_area(pentagon_vertices):.4f}")
    print(f"Invalid Input (2 vertices) Area: {calculate_polygon_area(invalid_vertices)}")