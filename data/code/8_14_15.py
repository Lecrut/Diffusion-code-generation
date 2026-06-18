import math

def calculate_polygon_area(coordinates):
    """
    Calculates the area of a polygon given its vertices in order using the Shoelace formula.
    
    Args:
        coordinates (list of tuples): List of (x, y) points defining the polygon vertices.
        
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

def main():
    """
    Main function to handle polygon input and calculation.
    Since direct interactive prompts are forbidden, this block uses hard-coded sample data
    as per the requirement constraints while demonstrating the logic flow.
    """
    # Hard-coded sample coordinates for a simple triangle (0,0), (4,0), (2,3)
    sample_coordinates = [
        (0, 0),
        (4, 0),
        (2, 3)
    ]

    print("Polygon Area Calculator")
    print(f"Processing polygon defined by {len(sample_coordinates)} vertices.")
    
    area = calculate_polygon_area(sample_coordinates)
    
    # Output the result efficiently to stdout
    if sample_coordinates:
        print(f"The calculated area of the polygon is: {area:.2f}")

if __name__ == '__main__':
    main()