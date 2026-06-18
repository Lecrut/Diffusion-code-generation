import math

def calculate_polygon_area(vertices):
    """
    Calculates the area of a polygon given its vertices using the Shoelace formula.
    
    Parameters:
        vertices (list[tuple]): List of tuples representing [x, y] coordinates of vertices in order.
        
    Returns:
        float: The calculated area of the polygon. If input is invalid or empty, returns None.
    """
    if not isinstance(vertices, list) or len(vertices) < 3:
        return None
    
    for i in range(len(vertices)):
        x1, y1 = vertices[i]
        # Ensure next vertex exists (wrapping around to first index at end)
        x2, y2 = vertices[(i + 1) % len(vertices)]
        
        if not isinstance(x1, (int, float)) or not isinstance(y1, (int, float)):
            return None
            
    n = len(vertices)
    sum_terms = 0.0
    
    for i in range(n):
        x1 = vertices[i][0]
        y1 = vertices[i][1]
        x2 = vertices[(i + 1) % n][0]
        y2 = vertices[(i + 1) % n][1]
        
        sum_terms += (x1 * y2 - x2 * y1)
    
    area = abs(sum_terms) / 2.0
    
    return area

if __name__ == '__main__':
    # Sample polygon: square with vertices [(0,0), (4,0), (4,4), (0,4)]
    sample_vertices = [
        (0, 0),
        (4, 0),
        (4, 4),
        (0, 4)
    ]

    area_result = calculate_polygon_area(sample_vertices)

    if area_result is not None:
        print(f"The area of the polygon defined by vertices {sample_vertices} is: {area_result}")
    else:
        print("Invalid input or insufficient vertices.")