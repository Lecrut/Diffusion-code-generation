import sys

def calculate_polygon_area(coords):
    """
    Calculates the area of a polygon given its vertices using the Shoelace formula.
    
    Parameters:
        coords (list[float]): A list of [x, y] coordinate pairs representing vertices in order.
        
    Returns:
        float: The calculated area of the polygon.
    """
    n = len(coords)
    if n < 3:
        return None
    
    area = 0.5 * abs(
        sum(
            coords[i][0] * coords[(i + 1) % n][1] -
            coords[(i + 1) % n][0] * coords[i][1]
            for i in range(n)
        )
    )
    
    return area

def main():
    # Hard-coded sample coordinates defining a simple quadrilateral (trapezoid-like shape)
    SAMPLE_COORDS = [
        [0, 0],
        [4, 0],
        [5, 3],
        [1, 2]
    ]

    print("Processing polygon area calculation for predefined sample coordinates.")
    
    # Extracting x and y lists from the sample coords for clarity in demonstration
    xs = [coord[0] for coord in SAMPLE_COORDS]
    ys = [coord[1] for coord in SAMPLE_COORDS]
    
    area_value = calculate_polygon_area(SAMPLE_COORDS)

    if not isinstance(area_value, float):
        print("Error: Not enough coordinates provided to form a polygon.")
    else:
        print(f"Polygon vertices (x, y): {SAMPLE_COORDS}")
        print(f"Calculated Area: {area_value} square units")

if __name__ == '__main__':
    main()