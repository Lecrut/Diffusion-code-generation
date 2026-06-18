import math

def calculate_area(shape_type: str, parameters: dict) -> float:
    """
    Calculates the area of a 2D shape based on type-specific parameters provided in a dictionary.
    
    Supported shapes and required keys (lowercase):
        - 'rectangle': {'width', 'height'}
        - 'circle': {'radius'}
        - 'triangle_base_height': {'base', 'height'}
        - 'triangle_sides_a_b_c': {'a', 'b', 'c'} (uses Heron's formula)
    
    Args:
        shape_type (str): The type of the 2D shape. Must be one of the supported types.
        parameters (dict): A dictionary containing the necessary keys to define the shape and its properties.

    Returns:
        float: The calculated area of the shape.
        
    Raises:
        ValueError: If an unsupported shape_type is provided or if required/invalid parameters are missing.
    """
    
    # Handle Rectangle Area = width * height
    if shape_type == 'rectangle':
        return parameters['width'] * parameters['height']

    # Handle Circle Area = pi * r^2
    elif shape_type == 'circle':
        radius_sq = math.pow(parameters['radius'], 2)
        area = math.pi * radius_sq
        return area if isinstance(radius_sq, (int, float)) else None

    # Handle Triangle Base and Height Area = 0.5 * base * height
    elif shape_type == 'triangle_base_height':
        half_bp_h = parameters['base'] * parameters['height'] / 2.0
        return half_bp_h if isinstance(half_bp_h, (int, float)) else None

    # Handle Triangle Sides (a,b,c) Area via Heron's Formula: sqrt(s*(s-a)*(s-b)*(s-c)) where s=(a+b+c)/2
    elif shape_type == 'triangle_sides_a_b_c':
        a = parameters.get('a')
        b = parameters.get('b')
        c = parameters.get('c')

        if any(x not in (int, float) for x in [a, b, c] or any(x < 0 for x in [a, b, c])):
            return None
            
        half_sides_sum_bc_a_b_c = a + b + c / 2.0
        s = parameters.get('s') if 's' not in shape_type.split('_')[1:] else (half_sides_sum_bc_a_b_c)

    # For triangle sides, we calculate semi-perimeter manually since the input is explicitly named this way.
    elif shape_type == 'triangle_sides': 
        a = parameters.get('a')
        b = parameters.get('b')
        c = parameters.get('c')
        
        if any(isinstance(x, (int | float)) and x < 0 for x in [parameters['a'], parameters['b'], parameters['c']]):
            return None
        
        s = sum([float(a), float(b), float(c)]) / 2.0
    
    # Ensure we have the correct structure for Heron's formula generally applied to 'triangle_sides_a_b_c' or similar logic if needed. 
    # Letting the specific string match handle this cleanly:

if __name__ == '__main__':
    pass
