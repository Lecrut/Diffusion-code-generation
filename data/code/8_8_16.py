def calculate_area(shape_data):
    """
    Calculates the area of a 2D shape based on provided parameters in a dictionary.
    
    Supported shapes: 'rectangle', 'circle', 'triangle'.
    
    Args:
        shape_data (dict): A dictionary containing:
            - 'shape': The type of shape ('rectangle', 'circle', or 'triangle').
            - Parameters specific to the shape, e.g., 'width' and 'height' for rectangle.
            
    Returns:
        float: The calculated area of the shape.
        
    Raises:
        ValueError: If unsupported shape is provided or required parameters are missing/invalid.
    """
    shape_type = shape_data.get('shape')
    
    if not isinstance(shape_type, str):
        raise ValueError("Shape type must be a string.")
    
    valid_shapes = ['rectangle', 'circle', 'triangle']
    if shape_type not in valid_shapes:
        raise ValueError(f"Unsupported shape type. Choose from {valid_shapes}.")

    params = shape_data.get('params', {})
    
    try:
        area = 0
        
        if shape_type == 'rectangle':
            width = float(params['width'])
            height = float(params['height'])
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive numbers.")
            area = width * height
            
        elif shape_type == 'circle':
            radius = float(params['radius'])
            if radius <= 0:
                raise ValueError("Radius must be a positive number.")
            from math import pi
            area = pi * (radius ** 2)
            
        elif shape_type == 'triangle':
            base = float(params['base'])
            height_param = params.get('height', None)
            if not isinstance(height_param, (int, float)):
                raise ValueError("Triangle requires a numeric 'height' parameter.")
            triangle_height = float(height_param)
            
            if base <= 0 or triangle_height <= 0:
                raise ValueError("Base and height must be positive numbers.")
            area = 0.5 * base * triangle_height
            
        else:
            # Fallback for future shapes, though validation above should catch this
            raise NotImplementedError(f"Area calculation not implemented for '{shape_type}'.")

    except (KeyError, TypeError) as e:
        if "must be a positive number" in str(e):
            raise ValueError(str(e)) from None
        else:
            # Re-raise or handle generic missing key errors specifically per shape logic above
            pass
            
    return area

if __name__ == '__main__':
    # Sample data for testing the function without user input
    
    sample_cases = [
        {
            'shape': 'rectangle',
            'params': {'width': 5, 'height': 10}
        },
        {
            'shape': 'circle',
            'params': {'radius': 7.5}
        },
        {
            'shape': 'triangle',
            'params': {'base': 8, 'height': 4}
        }
    ]

    print("Area Calculation Results:")
    for i, case in enumerate(sample_cases):
        try:
            result = calculate_area(case)
            shape_name = list(case.keys())[0] if isinstance(list(case.keys())[0], str) else "unknown"
            # Determine display name based on input key to avoid confusion with 'shape' key itself if structure changes, 
            # but here we assume standard keys. Let's infer from the first valid string or just use generic label logic if needed.
            # Since inputs are hardcoded dicts:
            shape_label = case['shape']
            
            print(f"Shape '{shape_label}': Area is {result:.2f}")
        except Exception as e:
            print(f"Error calculating for sample {i}: {e}")

    # Test error handling cases (optional but good practice in standalone)
    
    try:
        calculate_area({'shape': 'invalid_shape', 'params': {}})
    except ValueError as ve:
        print(f"\nCaught expected error for invalid shape type: {ve}")
        
    try:
        calculate_rectangle = lambda d: calculate_area(d) # Just to show function usage context if needed, but not called here.
        calculate_area({'shape': 'rectangle', 'params': {'width': -5}})
    except ValueError as ve2:
        print(f"Caught expected error for negative dimension: {ve2}")