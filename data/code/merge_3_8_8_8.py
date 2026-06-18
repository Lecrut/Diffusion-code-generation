"""General-purpose area calculation function for various 2D shapes."""

def calculate_area(shape_type: str, parameters: dict) -> float:
    """
    Calculate the area of a 2D shape based on its type and defining parameters.

    Supported shapes:
        - 'rectangle': requires {'width', 'height'}
        - 'circle': requires {'radius'}
        - 'triangle': requires {'base', 'height'}
        - 'trapezoid': requires {'a', 'b', 'h'} (parallel sides a and b, height h)

    Args:
        shape_type (str): The type of the shape. Must be one of 
                          'rectangle', 'circle', 'triangle', or 'trapezoid'.
        parameters (dict): A dictionary containing the defining parameters for the shape.

    Returns:
        float: The calculated area of the shape.

    Raises:
        ValueError: If an unsupported shape type is provided, 
                   if required parameters are missing, or if any parameter value is invalid.
    """
    
    # Validate shape type
    valid_shapes = ['rectangle', 'circle', 'triangle', 'trapezoid']
    if shape_type not in valid_shapes:
        raise ValueError(f"Unsupported shape type '{shape_type}'. "
                        f"Supported types are {valid_shapes}")

    area = 0.0
    
    try:
        # Handle Rectangle
        if shape_type == 'rectangle':
            width = parameters.get('width')
            height = parameters.get('height')
            
            if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                raise ValueError("Width and height must be numeric values.")
            if width <= 0 or height <= 0:
                raise ValueError("Dimensions must be positive numbers.")
                
            area = width * height

        # Handle Circle
        elif shape_type == 'circle':
            radius = parameters.get('radius')
            
            if not isinstance(radius, (int, float)):
                raise ValueError("Radius must be a numeric value.")
            if radius <= 0:
                raise ValueError("Radius must be positive.")
                
            area = 3.141592653589793 * radius ** 2

        # Handle Triangle
        elif shape_type == 'triangle':
            base = parameters.get('base')
            height = parameters.get('height')
            
            if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
                raise ValueError("Base and height must be numeric values.")
            if base <= 0 or height <= 0:
                raise ValueError("Dimensions must be positive numbers.")
                
            area = 0.5 * base * height

        # Handle Trapezoid
        elif shape_type == 'trapezoid':
            a = parameters.get('a')
            b = parameters.get('b')
            h = parameters.get('h')
            
            if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
                raise ValueError("Parallel sides and height must be numeric values.")
            if a <= 0 or b <= 0 or h <= 0:
                raise ValueError("Dimensions must be positive numbers.")
                
            area = 0.5 * (a + b) * h

        else:
            # This part is theoretically unreachable due to earlier validation, 
            # but kept for structural completeness if new shapes are added later.
            raise NotImplementedError(f"Area calculation not implemented for '{shape_type}'.")

    except Exception as e:
        raise ValueError(f"Error calculating area of {shape_type}: {str(e)}") from None
    
    return float(area)

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required.
    
    shapes_to_test = [
        ('rectangle', {'width': 5, 'height': 3}),
        ('circle', {'radius': 4}),
        ('triangle', {'base': 10, 'height': 6}),
        ('trapezoid', {'a': 8, 'b': 2, 'h': 5})
    ]

    print("Area Calculation Results:")
    for shape_type, params in shapes_to_test:
        try:
            area = calculate_area(shape_type, params)
            # Using f-string to format the output cleanly. 
            # For circle we use pi approximation from calculation logic (3.14...), 
            # but standard math.pi is more precise for display if needed.
            print(f"Shape '{shape_type}' with {params}: Area = {area:.2f}")
        except ValueError as ve:
            print(f"Error calculating area of shape '{shape_type}': {ve}")

    # Test an invalid case to demonstrate error handling
    try:
        calculate_area('square', {'side_length': 5})
    except ValueError as e:
        print(f"\nExpected error for unsupported parameter in 'rectangle' logic (if treated generically):")
        print(e)