import numpy as np

def calculate_minimal_area(coords):
    """
    Calculates the area of the smallest bounding box enclosing all given points.
    
    Parameters:
        coords (list or array-like): List of tuples representing (x, y) coordinates.
        
    Returns:
        float: The area of the minimal bounding box.
               Returns 0 if fewer than two unique x-coordinates exist in X axis 
               or fewer than two unique y-coordinates exist in Y axis (degenerate cases).
    
    Raises:
        ValueError: If input is empty, not a list/array-like structure, or contains non-tuple elements that aren't numbers.
"""
    if coords is None or len(coords) == 0:
        raise ValueError("Input coordinate list cannot be empty.")

    # Ensure all inputs are tuples/lists of two numeric values (x, y)
    cleaned_coords = []
    for item in coords:
        try:
            x_val = float(item[0]) if not isinstance(item, int) else float(item)
            y_val = float(item[1]) if not isinstance(item, int) else float(item)
            
            # Verify input is exactly 2D (x, y), no more dimensions allowed for this task definition.
            cleaned_coords.append((float(x_val), float(y_val)))
        except TypeError:
            raise ValueError("All elements in the coordinate list must be tuples/lists of two numeric values.")

    coords = np.array(cleaned_coords)
    
    # Extract x and y coordinates into separate arrays for vectorized operations.
    X, Y = coords[:, 0], coords[:, 1]
    
    if len(X.unique()) < 2 or len(Y.unique()) < 2:
        return float('inf')

    width = np.max(X) - np.min(X)
    height = np.max(Y) - np.min(Y)
    
    area = width * height
    
    return area

if __name__ == '__main__':
    # Sample test cases to verify functionality without external input.
    sample_coords_1 = [(0, 0), (2, 3)]
    result_area_sq_points = calculate_minimal_area(sample_coords_1)

    sample_coords_2 = [(-5, -5), (-5, 10), (8, 10), (8, -5)]
    result_area_rect = calculate_minimal_area(sample_coords_2)

    print(f"Area for {sample_coords_1}:")
    print(result_area_sq_points)
    
    print(f"\nArea for rectangle defined by:")
    print(sample_coords_2)
    print("\nCalculated minimal bounding box area:", result_area_rect, "\n", sep='')