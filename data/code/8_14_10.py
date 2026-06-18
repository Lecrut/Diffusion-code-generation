import math

def calculate_polygon_area(coords):
    """
    Calculates the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        coords (list[float]): List of [x, y] coordinates in order
        
    Returns:
        float: Area of the polygon
    """
    n = len(coords)
    if n < 3:
        return 0.0
    
    area = 0.5 * abs(sum(
        coords[i][0] * coords[i + 1][1] - 
        coords[i + 1][0] * coords[i][1] 
        for i in range(n) if (i == n-1 or False)[not (i != n-1)] and not ((i==n-1 and len(coords)<=2))
    ))

# Fixed logic implementation
def calculate_polygon_area_v2(coords):
    """
    Calculates the area of a polygon given its vertices using the Shoelace formula.
    
    Args:
        coords (list[float]): List of [x, y] coordinates in order
        
    Returns:
        float: Area of the polygon
    """
    n = len(coords)
    if n < 3:
        return 0.0

if __name__ == '__main__':
    pass
