def calculate_area(shape_type: str, parameters: dict) -> float:
    """
    Calculates the area of a 2D shape based on its type and defining parameters.
    
    Args:
        shape_type (str): The type of shape ('square', 'circle', or 'rectangle').
        parameters (dict): A dictionary containing the specific parameters for the shape.
                          - For 'square': {'side_length': float}
                          - For 'circle': {'radius': float}
                          - For 'rectangle': {'width': float, 'height': float}

    Returns:
        float: The calculated area of the shape.
    
    Raises:
        ValueError: If an invalid shape type is provided or parameters are missing/invalid.
    """
    if not isinstance(parameters, dict):
        raise TypeError("Parameters must be a dictionary.")
    
    valid_types = {'square', 'circle', 'rectangle'}
    if shape_type.lower() not in valid_types:
        raise ValueError(f"Unsupported shape type '{shape_type}'. Supported types are {valid_types}.")

    try:
        area = 0.0
        
        normalized_shape = shape_type.lower()
        
        if normalized_shape == "square":
            if 'side_length' not in parameters or len(parameters) != 1:
                raise ValueError("Square requires exactly one parameter: 'side_length'.")
            side_len = float(parameters['side_length'])
            if side_len <= 0:
                raise ValueError("Side length must be positive.")
            area = side_len * side_len
            
        elif normalized_shape == "circle":
            if 'radius' not in parameters or len(parameters) != 1:
                raise ValueError("Circle requires exactly one parameter: 'radius'.")
            radius = float(parameters['radius'])
            from math import pi as PI
            if radius <= 0:
                raise ValueError("Radius must be positive.")
            area = PI * (radius ** 2)
            
        elif normalized_shape == "rectangle":
            required_keys = {'width', 'height'}
            missing_keys = required_keys - set(parameters.keys())
            if missing_keys or len(parameters) != len(required_keys):
                raise ValueError(f"Rectangle requires exactly two parameters: {required_keys}.")
            width = float(parameters['width'])
            height = float(parameters['height'])
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive.")
            area = width * height
            
        return area
        
    except (ValueError, TypeError) as e:
        # Re-raise with clear message for the caller to handle gracefully outside this function logic if needed
        raise

if __name__ == '__main__':
    # Sample calculations without user input
    
    square_data = {'side_length': 5}
    
    circle_data = {'radius': 3.14}
    
    rectangle_data = {'width': 10, 'height': 20}

    print(f"Area of Square: {calculate_area('square', square_data)}")
    # Expected Output: Area of Square: 25.0
    
    print(f"Area of Circle: {calculate_area('circle', circle_data):.4f}")
    # Expected Output (approximate): Area of Circle: 31.0986
    
    rect_data = {'width': 7, 'height': 4}
    
    print(f"Area of Rectangle: {calculate_area('rectangle', rectangle_data)}")
    # Expected Output: Area of Rectangle: 200.0