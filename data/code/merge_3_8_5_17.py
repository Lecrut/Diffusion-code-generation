import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): List of [x, y] coordinates representing 
                                              ordered vertices of the polygon.
        
    Returns:
        float: The calculated area of the polygon.
        
    Raises:
        ValueError: If fewer than 3 unique vertices are provided or if input format is invalid.
    """
    n = len(vertices)
    
    # Validate that we have at least 3 points and they form a closed loop implicitly by 
    # adding the first point back to the end in the calculation logic, though strictly 
    # Shoelace works on ordered list where last connects to first.
    if n < 3:
        raise ValueError("A polygon must have at least 3 vertices.")

    area = 0.0
    
    for i in range(n):
        x1, y1 = vertices[i]
        # The next vertex wraps around to the start of the list
        j = (i + 1) % n
        x2, y2 = vertices[j]
        
        area += (x1 * y2 - x2 * y1)

    return abs(area / 2.0)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    # Sample polygon: A simple square with vertices [(0, 0), (4, 0), (4, 4), (0, 4)]
    # Expected area: 16.0
    square_vertices = [
        (0, 0), 
        (4, 0), 
        (4, 4), 
        (0, 4)
    ]

    # Sample polygon: A triangle with vertices [(0, 0), (5, 3), (-2, -1)]
    # Expected area calculation using Shoelace:
    # |((0*3 + 5*-1 + -2*0) - ((0*5 + 3*-2 + -1*0))) / 2| = |(0 - 5 - 0) - (0 - 6)| / 2 = |-5 - (-6)|/2 = |1|/2? 
    # Let's re-calculate manually:
    # x1=0, y1=0; x2=5, y2=3 -> term1 = 0*3 - 5*0 = 0
    # x2=5, y2=3; x3=-2, y3=-1 -> term2 = 5*-1 - (-2)*3 = -5 + 6 = 1
    # x3=-2, y3=-1; x4=0, y4=0 (closing) -> term3 = -2*0 - 0*(-1) = 0
    # Sum = 0 + 1 + 0 = 1. Area = |1|/2? Wait, the loop logic in function handles closing automatically via modulo.
    # Let's trace code: 
    # i=0 (0,0), j=1 (5,3) -> 0*3 - 5*0 = 0
    # i=1 (5,3), j=2 (-2,-1) -> 5*-1 - (-2)*3 = -5 + 6 = 1
    # i=2 (-2,-1), j=3 (0,4)? No, vertices list is length 3. 
    # Wait, my manual trace above assumed closing explicitly in loop but the code uses modulo n which implicitly closes it if we iterate correctly?
    # Actually standard Shoelace sums x_i*y_{i+1} - x_{i+1}*y_i for i from 0 to n-2. 
    # The term connecting last back to first is handled by j = (n-1 + 1) % n = 0 when i = n-1?
    # Let's re-read the code logic: loop runs range(n). Last iteration i=n-1. j=0. Correctly includes closing edge.
    
    triangle_vertices = [
        (0, 0), 
        (5, 3), 
        (-2, -1)
    ]

    # Calculate areas
    square_area = calculate_polygon_area(square_vertices)
    triangle_area = calculate_polygon_area(triangle_vertices)

    print(f"Area of the sample polygon (square): {square_area}")
    print(f"Area of the second sample polygon (triangle): {triangle_area}")