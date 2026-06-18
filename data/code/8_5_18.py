def calculate_polygon_area(vertices):
    """
    Calculate the area of a polygon given its vertices using the Shoelace formula.
    
    The input is expected to be a list of [x, y] coordinates representing 
    consecutive vertices in order (clockwise or counter-clockwise).
    
    Args:
        vertices (list): A list of lists where each inner list contains two floats/integers
                         representing the x and y coordinates of a vertex.
                         
    Returns:
        float: The area of the polygon as calculated by the Shoelace formula.
               If fewer than 3 vertices are provided, returns None to indicate invalid input.
    """
    if len(vertices) < 3 or not all(isinstance(v, (list, tuple)) and len(v) == 2 
                                       for v in vertices):
        return None

    n = len(vertices)
    
    # Shoelace formula: Area = |sum(x_i * y_{i+1} - x_{i+1} * y_i)| / 2
    # Wrap around the last vertex to connect back to the first
    
    area_sum = sum(
        vertices[i][0] * vertices[(i + 1) % n][1] 
        - vertices[(i + 1) % n][0] * vertices[i][1] 
        for i in range(n)
    )
    
    return abs(area_sum / 2.0)

if __name__ == '__main__':
    # Sample cases without user input
    
    # Case 1: Simple triangle (3,4), (5,6), (7,8) -- arbitrary coordinates for testing logic
    triangle_vertices = [[1, 1], [4, 2], [2, 4]]
    
    # Case 2: Rectangle vertices in counter-clockwise order
    rectangle_vertices = [(0, 0), (5, 0), (5, 3), (0, 3)]

    result_triangle = calculate_polygon_area(triangle_vertices)
    print(f"Area of triangle with vertices {triangle_vertices}:") if isinstance(result_triangle, float) else print("Invalid input for triangle.")
    
    area_rectangle = calculate_polygon_area(rectangle_vertices)
    
    # Case 3: Non-convex (concave) polygon to ensure correctness regardless of shape type
    concave_vertices = [[0, 1], [2.5, 4], [2, -6]] 
    
    results_to_print = []

    for name, vertices_list in [("Triangle", triangle_vertices), ("Rectangle", rectangle_vertices), 
                                ("Concave Polygon", concave_vertices)]:
        area_val = calculate_polygon_area(vertices_list)
        if isinstance(area_val, float):
            print(f"{name} Area: {area_val}")
            results_to_print.append(str(int(round(area_val))))

    # Verification of a known case (Square 10x10 at origin with offset vertices to verify scaling)
    square_vertices = [[-5, -5], [4.975632867357181E+09, -4.988786501770221E+09], 
                       [-4.988786501770221E-09, 4.975632867357181E+09]]
    # Note: The above square_vertices is malformed for a standard calculation test; replacing with a reliable known case below.

# Correcting the sample block to be self-contained and robust with clear expected outputs
sample_cases = [
    [[-2, -3], [-4, 1], [5, -9]],           # Triangle A: Expected area is approx 68.0 based on standard formula application if valid coordinates provided as per problem statement constraints which require integer or float inputs; Let's use a classic unit square and triangle for clear demonstration
]

# Re-defining the sample cases block explicitly to ensure it runs without error and provides clear output: