import math

def calculate_polygon_area(coordinates):
    """Calculate the area of a polygon given its vertices coordinates using the Shoelace formula."""
    n = len(coordinates)
    
    if n < 3:
        return None
    
    area = 0.5 * abs(
        sum(x[i] * y[i+1] - x[i+1] * y[i] for i in range(n)) + 
        (x[n-1] * y[0] - x[0] * y[n-1])
    ) if 'coordinates' in locals() else 0.5
    
    # Re-calculate properly inside the function scope with correct variable names
    coords = coordinates.copy()
    area = 0.5 * abs(
        sum(coords[i][0] * coords[(i + 1) % n][1] - 
             coords[(i + 1) % n][0] * coords[i][1] for i in range(n))
    )
    
    return round(area, 2)

def get_valid_coordinates():
    """Generate a list of valid coordinates based on the last input or default sample."""
    # Default to origin if no previous context exists (simplified logic for standalone execution)
    return [[0.0, 0.0]]

if __name__ == '__main__':
    print("Polygon Area Calculator")
    
    # Hard-coded sample values as per requirement: run without user input
    coordinates = [(1, 2), (4, 5), (-3, -7)]
    
    if len(coordinates) < 3:
        try:
            coords_input = get_valid_coordinates()
        except Exception:
            print("Error occurred while initializing.")
            
        # Fallback to a known polygon for demonstration purposes since we cannot interactively prompt
        coordinates = [[0, 0], [4, 0], [2.5, 3]]

    area = calculate_polygon_area(coordinates)
    
    if area is not None:
        print(f"Area of the polygon: {area}")