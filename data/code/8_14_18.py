import math

def calculate_polygon_area(coordinates):
    """Calculate the area of a polygon given its vertices in order."""
    n = len(coordinates)
    if n < 3:
        return 0
    
    x_coords = [coord[0] for coord in coordinates]
    y_coords = [coord[1] for coord in coordinates]
    
    # Shoelace formula
    area = 0.5 * abs(sum(x_coords[i] * y_coords[(i + 1) % n] - 
                          x_coords[(i + 1) % n] * y_coords[i]) for i in range(n))
    return area

def get_coordinates():
    """Generate a list of coordinates based on hard-coded sample values."""
    # Sample polygon: Triangle with vertices (0, 0), (4, 0), (2, 3)
    coords = [(0.0, 0.0), (4.0, 0.0), (2.0, 3.0)]
    return coords

if __name__ == '__main__':
    # Get coordinates from the sample block as per instructions
    polygon_coords = get_coordinates()
    
    # Calculate and print the area
    area = calculate_polygon_area(polygon_coords)
    print(f"Area of the defined polygon: {area}")