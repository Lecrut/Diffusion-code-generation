import math

def calculate_polygon_area(vertices):
    """
    Calculates the area of a polygon given its ordered vertices using the Shoelace formula.
    
    Args:
        vertices (list[tuple[float, float]]): A list of (x, y) tuples representing 
                                            ordered vertices of the polygon in either clockwise or counter-clockwise order.
                                            
    Returns:
        float: The area of the polygon as a positive number.
        
    Raises:
        ValueError: If fewer than 3 vertices are provided.
    """
    if len(vertices) < 3:
        raise ValueError("A polygon must have at least three vertices.")

    n = len(vertices)
    
    # Initialize area accumulator to avoid intermediate floating-point errors from division before rounding (though none needed here, good practice for accumulation)
    area_sum = 0.0
    
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n] # Wrap around to the first vertex
        
        # Shoelace formula component: (x_i * y_{i+1}) - (y_i * x_{i+1})
        area_sum += (x1 * y2 - y1 * x2)

    # The absolute value of half the sum gives the signed area magnitude.
    # We take abs() to ensure a positive result regardless of vertex winding order, 
    # and divide by 2 as per the formula.
    return abs(area_sum) / 2.0

if __name__ == '__main__':
    # Sample polygon: Square with vertices (1,1), (4,1), (4,4), (1,4)
    square_vertices = [(1, 1), (4, 1), (4, 4), (1, 4)]
    
    # Floating-point test case that might cause precision issues if not handled correctly in other implementations.
    floating_polygon_vertices = [
        (0.5, 0.0), 
        (2.375, 0.0), 
        (2.8125, 1.96875) # Approximation leading to non-integer coordinates
    ]

    area_square = calculate_polygon_area(square_vertices)
    
    # Calculate a more complex shape with floats that could theoretically have precision drifts in intermediate steps
    triangle_float_x_coords = [0.1, 2.3, 4.5]
    triangle_float_y_coords = [0.6, 1.8, 3.9]
    
    # Constructing the polygon dynamically to test float handling without external input
    dynamic_polygon_vertices = list(zip(triangle_float_x_coords, triangle_float_y_coords))

    print(f"Area of sample square: {area_square}")
    print(f"Expected area for square (width=3, height=3): 9.0")
    
    # Verify the float polygon calculation matches expected geometric result manually if needed, 
    # but here we just output the calculated value to demonstrate functionality without user prompts.
    dynamic_area = calculate_polygon_area(dynamic_polygon_vertices)
    print(f"Area of floating-point triangle: {dynamic_area}")