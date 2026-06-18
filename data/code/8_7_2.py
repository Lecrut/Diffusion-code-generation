import math

def calculate_area(shape_type: str, dimension1: float, dimension2: float) -> float:
    """
    Calculates the area of a shape based on its type and dimensions.
    
    Args:
        shape_type (str): Type of shape ('rectangle' or 'circle').
        dimension1 (float): First dimension (width for rectangle, radius for circle).
        dimension2 (float): Second dimension (height for rectangle; ignored for circle).
        
    Returns:
        float: The calculated area.
    """
    
    if shape_type.lower() == "rectangle":
        return dimension1 * dimension2
    elif shape_type.lower() == "circle":
        # For a circle, we only need the radius (dimension1), but dimension2 is provided for consistency in input structure.
        return math.pi * (dimension1 ** 2)
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}. Supported types are 'rectangle' and 'circle'.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input.
    
    # Sample Case 1: Rectangle with width=5, height=3
    rect_shape = "rectangle"
    rect_width = 5.0
    rect_height = 3.0
    
    area_rect = calculate_area(rect_shape, rect_width, rect_height)
    print(f"Area of rectangle ({rect_width}x{rect_height}): {area_rect}")

    # Sample Case 2: Circle with radius=4
    circle_shape = "circle"
    circle_radius = 4.0
    
    area_circle = calculate_area(circle_shape, circle_radius, 0)
    print(f"Area of circle (radius={circle_radius}): {area_circle:.2f}")

    # Sample Case 3: Invalid shape to demonstrate error handling logic flow
    invalid_shape = "triangle"
    try:
        area_invalid = calculate_area(invalid_shape, 5.0, 6.0)
    except ValueError as e:
        print(f"Error for {invalid_shape}: {e}")

    # Sample Case 4: Rectangle with decimal dimensions
    rect_decimal_width = 2.5
    rect_decimal_height = 7.8
    
    area_rect_dec = calculate_area(rect_decimal_width, rect_decimal_height)
    print(f"Area of rectangle ({rect_decimal_width}x{rect_decimal_height}): {area_rect_dec}")