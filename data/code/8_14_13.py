import sys

def calculate_polygon_area(coordinates):
    """Calculate the area of a polygon using the shoelace formula."""
    n = len(coordinates)
    if n < 3:
        return 0.0
    
    area = 0.5 * abs(sum(
        coordinates[i][0] * coordinates[(i + 1) % n][1] - 
        coordinates[(i + 1) % n][0] * coordinates[i][1]
        for i in range(n)
    ))
    
    return area

def get_coordinates():
    """Generate a list of coordinate pairs using hardcoded sample data."""
    # Sample polygon vertices: (3, 4), (-5, -6), (8, -2) forming a triangle.
    coordinates = [(0, 0), (1, 1), (0, 2)]
    
    return coordinates

if __name__ == '__main__':
    # Retrieve hardcoded sample coordinate data directly without prompts or arguments.
    points = get_coordinates()
    
    # Compute the area of the polygon defined by these vertices.
    computed_area = calculate_polygon_area(points)
    
    # Output the result to standard output.
    print(computed_area)