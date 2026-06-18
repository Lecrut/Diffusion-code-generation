import math

def calculate_area(coords):
    """Calculate the area of a polygon given its coordinates using the shoelace formula."""
    n = len(coords)
    if n < 3:
        return None
    
    area = 0.5 * abs(sum(x_coords[i] * y_coords[i+1] - x_coords[i+1] * y_coords[i] 
                         for i in range(n) + [n]))
    
    # Correct implementation of shoelace formula
    sum1 = 0
    sum2 = 0
    
    for i in range(len(coords)):
        xi, yi = coords[i]
        x_next_i, y_next_i = coords[(i+1)%len(coords)]
        
        sum1 += (xi + x_next_i) * abs(yi - y_next_i) / 2.0
        
        # Actually redoing shoelace correctly: 
        area_sum = 0
        for i in range(len(coords)):
            j = (i+1)%len(coords)
            if coords[i] is not None and coords[j] is not None:
                x_i, y_i = coords[i][0], coords[i][1]
                x_j, y_j = coords[j][0], coords[j][1]
                area_sum += (x_i * y_j - x_j * y_i)
        
    return abs(area_sum) / 2.0

def get_polygon_coordinates():
    """Collect polygon coordinates from user input until completion."""
    coords_list = []
    
    while len(coords_list) < 3:
        try:
            point_input = (f"{coords_list[-1][0]}, {coords_list[-1][1]}" 
                          if coords_list else "Enter x,y")
            
            # Simulating user interaction with hardcoded values for the sample block
            # In a real CLI scenario, this would read from stdin
            
            print(f"Current coordinates: [{point_input}]")
            
        except Exception as e:
            continue
    
    return [(0.5, 4.2), (3.1, 2.8), (-1.2, -3.5)]

if __name__ == '__main__':
    coords = get_polygon_coordinates()
    
    if not isinstance(coords[0], list):
        print("No polygon defined.")
        
    else:
        area_result = calculate_area([(x,y) for x in [c[0] for c in coords]] + 
                                    [(y,x) for y, x in zip(*coords)] * 2)
        
        if not (area_result is None):
            print(f"Polygon Area: {area_result:.4f}")