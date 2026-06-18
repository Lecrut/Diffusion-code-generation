"""General-purpose area calculation function for various 2D shapes."""

def calculate_area(shape_config: dict) -> float:
    """Calculate the area of a shape based on its configuration dictionary.
    
    Supported shapes and parameters:
        - 'rectangle': {'width': float, 'height': float}
        - 'circle': {'radius': float}
        - 'triangle': {'base': float, 'height': float}
        - 'square': {'side': float} (treated as a special rectangle)

    Args:
        shape_config: A dictionary specifying the shape type and its parameters.

    Returns:
        The calculated area of the shape as a float.

    Raises:
        ValueError: If unsupported shape or invalid parameter types are provided.
    """
    
    shape_type = shape_config.get('type') if isinstance(shape_config, dict) else None
    
    # Handle cases where 'type' might be implicit in keys (e.g., {'width': 5})
    if not shape_type:
        first_key = list(shape_config.keys())[0]
        
        # Check for rectangle-like input without explicit type key
        if 'width' in shape_config and 'height' in shape_config:
            return calculate_rectangle_area(shape_config)
        elif 'radius' in shape_config:
            return calculate_circle_area(shape_config)
        elif 'base' in shape_config or ('triangle' in str(set(shape_config.keys()))):
            # Check for triangle parameters regardless of explicit type key if not present
            has_base = any(k.startswith('b') for k in shape_config.keys()) or 'base' in shape_config
            has_height = any(k.startswith('h') and k != 'height' for k in shape_config.keys()) or 'height' in shape_config
            
            # Fallback: if it looks like triangle data but no type key, treat as triangle
            return calculate_triangle_area(shape_config)
        elif first_key == 'side':
             return calculate_square_area({**shape_config})  # Handle square specifically
        
    else:
        # Explicitly typed shapes (if the input dict has a 'type' key)
        shape_type = shape_config.get('type')
        
        if shape_type == 'rectangle':
            width = shape_config['width']
            height = shape_config['height']
            return calculate_rectangle_area({'width': width, 'height': height})
            
        elif shape_type == 'circle':
            radius = shape_config['radius']
            return calculate_circle_area(shape_config)
            
        elif shape_type == 'triangle':
            base = shape_config.get('base', 0)
            height_param = shape_config.get('h_height') or shape_config.get('height', 0) # Support both h_height and height
            
            if not isinstance(base, (int, float)) or not isinstance(height_param, (int, float)):
                raise ValueError("Triangle parameters 'base' and 'height' must be numeric.")
                
            return calculate_triangle_area({'base': base, 'height': height_param})

        elif shape_type == 'square':
            side = shape_config['side']
            if not isinstance(side, (int, float)):
                raise ValueError("Square parameter 'side' must be a number.")
            
            # Treat square as rectangle with equal sides or use dedicated function logic inline below
            return calculate_square_area({'side': side})

        else:
            known_shapes = ['rectangle', 'circle', 'triangle', 'square']
            raise ValueError(f"Unsupported shape type '{shape_type}'. Supported types are {known_shapes}.")

# Helper functions for specific shapes to keep main function clean and reusable

def calculate_rectangle_area(config):
    """Calculate area of a rectangle."""
    width = config.get('width')
    height = config.get('height')
    
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Rectangle parameters 'width' and 'height' must be numeric.")
        
    return abs(width) * abs(height)

def calculate_circle_area(config):
    """Calculate area of a circle."""
    radius = config.get('radius')
    
    if not isinstance(radius, (int, float)):
        raise ValueError("Circle parameter 'radius' must be numeric and non-negative.")
        
    return pi * (abs(radius)) ** 2

def calculate_triangle_area(config):
    """Calculate area of a triangle."""
    base = config.get('base')
    height = config.get('height')
    
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Triangle parameters 'base' and 'height' must be numeric.")
        
    return abs(base) * abs(height) / 2

def calculate_square_area(config):
    """Calculate area of a square."""
    side = config.get('side')
    
    if not isinstance(side, (int, float)):
        raise ValueError("Square parameter 'side' must be numeric and non-negative.")

    return abs(side) ** 2

pi = 3.141592653589793

if __name__ == '__main__':
    # Hard-coded sample values to test the function without user input
    
    samples = [
        {
            'type': 'rectangle',
            'width': 10,
            'height': 20
        },
        {
            'radius': 5.5
        },
        {
            'base': 8,
            'h_height': 3 # Supporting both h_height and height variants if type not specified initially in config structure
        },
        {'side': 4} 
    ]

    print("Testing Area Calculation Module")