import math

def calculate_polygon_area(coords):
    """
    Calculates the area of a polygon given its vertices in order using the Shoelace formula.
    
    Args:
        coords (list of tuples): List of (x, y) coordinates representing vertices in order.
        
    Returns:
        float: The calculated area of the polygon.
    """
    n = len(coords)
    if n < 3:
        return 0.0

    area = 0.5 * abs(
        sum(x[i] * y[(i + 1) % n] - x[(i + 1) % n] * y[i]) for i in range(n)
    )
    return area

def get_coords_iteratively():
    """
    Simulates the iterative input prompt by returning a predefined list of coordinates.
    
    Returns:
        list of tuples: List of (x, y) coordinates.
    """
    # Hard-coded sample values as per requirements to avoid any interactive prompts or sys.stdin calls
    return [(0, 0), (4, 0), (4, 3), (1, 3)]

if __name__ == '__main__':
    coords = get_coords_iteratively()
    
    print("Input coordinates provided.")
    area_result = calculate_polygon_area(coords)
    
    if not math.isfinite(area_result):
        print("Error: Invalid calculation result.")
    else:
        print(f"Area of polygon defined by the input vertices is {area_result:.2f}")