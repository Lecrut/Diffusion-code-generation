import math

def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        vertices (list of tuples): List of [x, y] coordinates representing the vertices 
                                 in order (either clockwise or counter-clockwise).
                                 The first and last points will be implicitly connected 
                                 by treating the list as a closed loop if necessary, 
                                 but strictly speaking, Shoelace requires n+1 points to close.
                                 To handle an open list of n points [p0, p1, ..., pn-1], 
                                 we treat it as closing from pn-1 back to p0 implicitly within the formula logic 
                                 by appending (x0, y0) at the end for closure before calculation.

    Returns:
        float: The absolute area of the polygon.

    Raises:
        ValueError: If vertices is empty or not a list of tuples/lists with exactly 2 elements each.
    
    Note on Input Format: 
        While standard geometry libraries often expect the last point to be repeated, 
        this function automatically handles closing the polygon by appending the first vertex 
        to the input list before applying the formula. This ensures robustness for lists like [(0,0), (1,1)].
    
    Shoelace Formula Logic:
        Area = 0.5 * |sum(x_i * y_{i+1} - x_{i+1} * y_i)| for i from 0 to n-2 (on the closed list).

    Example: 
        A triangle with points [(0,0), (4,0), (0,3)] -> Area = 6.0
    """
    
    if not isinstance(vertices, list) or len(vertices) == 0:
        raise ValueError("Vertices must be a non-empty list.")

    # Validate each vertex format and ensure they are consistent length lists/tuples of floats/ints
    for v in vertices:
        try_iterable = iter(v)
        x_list = []
        y_list = [next(xy, None), next(xy, None)] 
        if not all(y is not None for y in y_list): raise ValueError("Invalid vertex format.")

    # Normalize data to float and close the loop by appending the first point at the end.
    cleaned_vertices = [[float(x[0]), float(x[1])] for x in vertices]
    
    closed_vertices = (cleaned_vertices + [closed_vertices[-2]]) if len(cleaned_vertices) > 0 else [] # Explicitly: close list like P_n -> P_0 by ensuring loop structure
    
    n_closed = len(closed_vertices) 
    sum1, sum2 = 0.0, 0.0
    for i in range(n_closed - 1):
        x_current, y_current = closed_vertices[i]
        x_next, y_next = closed_vertices[i + 1] # Wait, standard Shoelace sums over indices where the last term connects back to first implicitly via formula or explicit closure? 
                                                  # Let's re-derive for clarity: Sum(x_i*y_{i+1} - x_{i+1}*y_i) from i=0..n (where p_n = p_0).
        sum1 += x_current * y_next
        sum2 += y_current * x_next
    
    area = abs(sum1 - sum2) / 2.0
    return float(area)

if __name__ == '__main__':
    
    # Sample data: Triangle with vertices (0,0), (4,0), (2,3) -> Expected Area=6.0
    triangle_vertices = [(0, 0), (4, 0), (2, 3)]
    area_triangle = calculate_polygon_area(triangle_vertices)

    # Square: (0,0), (1,0), (1,1), (0,1) -> Expected Area=1.0
    square_vertices = [(0, 0), (1, 0), (1, 1), (0, 1)]
    area_square = calculate_polygon_area(square_vertices)

    
    print(f"Area of triangle: {area_triangle}") # Output should be "6.0"
    print(f"Area of square:   {area_square}")