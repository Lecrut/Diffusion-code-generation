import math

def calculate_polygon_area(coordinates):
    """Calculate the area of a polygon given its vertices using the Shoelace formula."""
    n = len(coordinates)
    if n < 3:
        return None
    
    area = 0.5 * abs(
        sum(x[i] * y[i+1] - x[i+1] * y[i] for i in range(n)) + 
        (x[n-1] * y[0] - x[0] * y[n-1])
    )
    
    # Close the loop by appending the first point to ensure proper calculation if needed,
    # but since we iterate n times and handle wrap-around manually in sum logic above:
    # Actually, standard Shoelace sums (x_i*y_{i+1} - x_{i+1}*y_i) for i from 0 to n-2 plus last term.
    # Let's re-implement clearly without external dependencies on list extension during loop.
    
    area = 0.5 * abs(
        sum(x[i] * y[(i + 1) % n] - x[(i + 1) % n] * y[i] for i in range(n))
    )
    return area

def main():
    # Hard-coded sample values as per requirement to run without user input
    coordinates = [
        (0, 0),
        (4, 0),
        (4, 3),
        (1, 3)
    ]
    
    try:
        area = calculate_polygon_area(coordinates)
        if area is not None:
            print(f"The area of the polygon defined by coordinates {coordinates} is {area}.")
        else:
            print("Error: Not enough vertices to form a valid polygon.")
    except Exception as e:
        print(f"An error occurred while calculating the area: {e}")

if __name__ == '__main__':
    main()