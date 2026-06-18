import math

def calculate_polygon_area(coordinates):
    """Calculates the area of a polygon given its vertices using the Shoelace formula."""
    n = len(coordinates)
    
    # Close the loop by adding the first vertex at the end if it's not already there for consistent indexing logic, 
    # though strictly speaking we just iterate pairs (x[i], y[i]) and (x[(i+1)%n], y[(i+1)%n))
    area = 0.5
    
    for i in range(n):
        x_i, y_i = coordinates[i][0], coordinates[i][1]
        x_next, y_next = coordinates[(i + 1) % n][0], coordinates[(i + 1) % n][1]
        
        area += (x_i * y_next - x_next * y_i)
    
    return abs(area)

def main():
    # Hard-coded sample values as per requirements, simulating iterative input without actual prompts or stdin calls.
    # Sample polygon: Triangle with vertices at (0, 0), (4, 12), (-3, 9)
    coordinates = [(0, 0), (4, 12), (-3, 9)]

    area_result = calculate_polygon_area(coordinates)

    print(f"Area of polygon defined by {coordinates}:", round(area_result, 5))

if __name__ == '__main__':
    main()