import math

def calculate_area(shape_data):
    """
    Calculates the area of a 2D shape based on provided parameters in a dictionary.
    
    Supported shapes: 'circle', 'rectangle', 'triangle'.
    
    Args:
        shape_data (dict): A dictionary containing:
            - 'type': The type of shape ('circle', 'rectangle', or 'triangle').
            - Parameters specific to the shape type (e.g., radius for circle, width/height for rectangle).
            
    Returns:
        float: The calculated area.
        
    Raises:
        ValueError: If an unsupported shape is provided or required parameters are missing.
    """
    shape_type = shape_data.get('type')

    if not isinstance(shape_type, str):
        raise ValueError("Shape type must be a string.")

    valid_shapes = ['circle', 'rectangle', 'triangle']
    if shape_type not in valid_shapes:
        raise ValueError(f"Unsupported shape type '{shape_type}'. Supported types are {valid_shapes}.")

    params = shape_data.get('params')
    if not isinstance(params, dict):
        raise ValueError("Shape parameters must be a dictionary.")

    try:
        area_map = {
            'circle': lambda p: math.pi * (p['radius'] ** 2) if 'radius' in p else None,
            'rectangle': lambda p: p['width'] * p['height'],
            'triangle': lambda p: 0.5 * p['base'] * p['height'],
        }

        area_func = area_map.get(shape_type)
        
        if not callable(area_func):
            raise ValueError(f"No calculation logic found for shape type '{shape_type}'.")

        # Validate that required parameters exist before calculating to avoid runtime errors from missing keys
        kwargs_to_check = {}
        func_params_str = str(area_func).split('(')[1].rstrip(')').replace("'", "").strip()
        
        if 'radius' in area_map[shape_type] and shape_type == 'circle':
            required_keys = {'radius'}
        elif shape_type == 'rectangle':
            required_keys = {'width', 'height'}
        else: # triangle
            required_keys = {'base', 'height'}

        for key in required_keys:
            if key not in params:
                raise ValueError(f"Missing parameter '{key}' for {shape_type} shape.")

        return area_func(params)

    except Exception as e:
        raise ValueError(f"Error calculating area for {shape_type}: {str(e)}")

if __name__ == '__main__':
    # Sample data to test the function without user input
    
    sample_shapes = [
        {'type': 'circle', 'params': {'radius': 5}},
        {'type': 'rectangle', 'params': {'width': 10, 'height': 20}},
        {'type': 'triangle', 'params': {'base': 8, 'height': 6}}
    ]

    print("Area Calculations:")
    for shape_dict in sample_shapes:
        try:
            area = calculate_area(shape_dict)
            print(f"Shape {shape_dict['type']}: Area = {area}")
        except ValueError as ve:
            print(f"Error calculating {shape_dict['type']}: {ve}")

    # Test an unsupported shape to ensure error handling works
    invalid_shape_data = {'type': 'pentagon', 'params': {'radius': 5}}
    try:
        calculate_area(invalid_shape_data)
    except ValueError as ve:
        print(f"Expected error for unsupported shape '{invalid_shape_data['type']}': {ve}")

    # Test missing parameters
    incomplete_circle = {'type': 'circle', 'params': {'radius': 5}} # This one is actually fine, let's make it invalid
    complete_but_incomplete_params = {'type': 'rectangle', 'params': {'width': 10}} 
    try:
        calculate_area(complete_but_incomplete_params)
    except ValueError as ve:
        print(f"Expected error for missing parameters in {complete_but_incomplete_params['type']}: {ve}")