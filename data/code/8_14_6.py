import math

def calculate_polygon_area(coordinates):
    """
    Calculates the area of a polygon given its vertices in order using the Shoelace formula.
    
    Args:
        coordinates (list of tuples): List of [x, y] pairs representing vertices in counter-clockwise or clockwise order.
        
    Returns:
        float: The calculated area of the polygon.
    """
    n = len(coordinates)
    if n < 3:
        return 0.0

    area = 0.5 * abs(sum(
        coordinates[i][0] * coordinates[(i + 1) % n][1] - 
        coordinates[(i + 1) % n][0] * coordinates[i][1]
        for i in range(n)
    ))
    
    return area

def main():
    # Hard-coded sample values to ensure the script runs without user input or external dependencies.
    # These represent a simple triangle with vertices at (0, 0), (4, 0), and (2, 3).
    sample_coordinates = [
        (0, 0), 
        (4, 0), 
        (2, 3)
    ]

    area_result = calculate_polygon_area(sample_coordinates)
    
    print(f"Area of the polygon: {area_result}")

if __name__ == '__main__':
    main()