def calculate_area(shape_data):
    """
    Calculates the area of a 2D shape based on provided parameters in a dictionary.
    
    Supported shapes: 'rectangle', 'circle', 'triangle'.
    
    Args:
        shape_data (dict): A dictionary containing:
            - 'shape_type': str, one of 'rectangle', 'circle', or 'triangle'
            - Parameters specific to the shape type
            
    Returns:
        float: The calculated area.
        
    Raises:
        ValueError: If unsupported shape type is provided or parameters are missing/invalid.
    """
    shape_type = shape_data.get('shape_type')

    if shape_type == 'rectangle':
        width = shape_data.get('width', 0)
        height = shape_data.get('height', 0)
        return width * height
        
    elif shape_type == 'circle':
        radius = shape_data.get('radius', 0)
        import math
        if radius < 0:
            raise ValueError("Radius must be non-negative.")
        return math.pi * (radius ** 2)
        
    elif shape_type == 'triangle':
        base = shape_data.get('base', 0)
        height_param = shape_data.get('height', 0)
        if not isinstance(base, (int, float)) or not isinstance(height_param, (int, float)):
            raise ValueError("Base and height must be numeric.")
        return 0.5 * base * height_param
        
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}. Supported types are 'rectangle', 'circle', 'triangle'.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values, no user input required
    
    sample_cases = [
        {'shape_data': {'shape_type': 'rectangle', 'width': 5.0, 'height': 3.0}},
        {'shape_data': {'shape_type': 'circle', 'radius': 4.2}},
        {'shape_data': {'shape_type': 'triangle', 'base': 10, 'height': 6}},
    ]

    for case in sample_cases:
        result = calculate_area(case['shape_data'])
        print(f"Area of {case['shape_data']['shape_type']}: {result}")