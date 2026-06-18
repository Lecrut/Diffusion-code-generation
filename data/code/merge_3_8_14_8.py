import math

def calculate_polygon_area(coordinates):
    """
    Calculates the area of a polygon given its vertices in order using the Shoelace formula.
    
    Args:
        coordinates (list[list[float]]): List of [x, y] pairs representing vertices.
        
    Returns:
        float: The calculated area of the polygon.
    """
    n = len(coordinates)
    if n < 3:
        return 0.0

    area = 0.5 * abs(sum(
        coordinates[i][0] * coordinates[(i + 1) % n][1] - 
        coordinates[i][1] * coordinates[(i + 1) % n][0]
        for i in range(n)
    ))
    
    return area

def get_sample_coordinates():
    """
    Returns a list of hardcoded sample coordinate points to form a triangle.
    Points: (0, 0), (4, 0), (2, 3) forming an equilateral-like shape for demonstration.
    """
    # Sample values as per requirement: no user input needed in this block
    return [[0.0, 0.0], [4.0, 0.0], [2.0, 3.0]]

if __name__ == '__main__':
    # Hard-coded sample coordinates for the main execution block
    sample_coords = get_sample_coordinates()
    
    area_result = calculate_polygon_area(sample_coords)
    
    print(f"Area of polygon: {area_result}")