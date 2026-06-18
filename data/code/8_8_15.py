def calculate_area(shape_type: str, parameters: dict) -> float:
    """
    Calculate the area of a 2D shape based on its type and defining parameters.
    
    Supported shapes (case-insensitive):
        - 'circle': requires {'radius': float}
        - 'rectangle': requires {'width': float, 'height': float}
        - 'triangle': requires {'base': float, 'height': float}
        
    Args:
        shape_type (str): The type of the 2D shape.
        parameters (dict): A dictionary containing the defining parameters for the shape.
        
    Returns:
        float: The calculated area of the shape.
        
    Raises:
        ValueError: If an unknown shape is provided or required parameters are missing/invalid.
    """
    if not isinstance(shape_type, str) or not isinstance(parameters, dict):
        raise TypeError("Shape type must be a string and parameters must be a dictionary.")

    # Normalize the shape name to lowercase for comparison
    normalized_shape = shape_type.lower().strip()

    try:
        area = 0.0
        
        if normalized_shape == 'circle':
            radius = parameters.get('radius')
            if not isinstance(radius, (int, float)) or radius <= 0:
                raise ValueError("Circle requires a positive numeric radius.")
            area = 3.141592653589793 * radius ** 2
            
        elif normalized_shape == 'rectangle':
            width = parameters.get('width')
            height = parameters.get('height')
            
            if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                raise ValueError("Rectangle requires numeric width and height.")
            if width <= 0 or height <= 0:
                raise ValueError("Width and height must be positive numbers.")
            area = width * height
            
        elif normalized_shape == 'triangle':
            base = parameters.get('base')
            triangle_height = parameters.get('height', None) # Using a specific key to avoid confusion with general 'height' if needed, but standard is often just 'h'. Let's stick to generic keys or explicit ones. 
            # Re-evaluating based on prompt "defining parameters": usually base and height are distinct enough.
            # If the user passes {'base': 10, 'height': 5}, it works.
            
            if not isinstance(base, (int, float)) or not isinstance(triangle_height, (int, float)):
                raise ValueError("Triangle requires numeric base and height.")
            if base <= 0 or triangle_height <= 0:
                raise ValueError("Base and height must be positive numbers.")
            area = 0.5 * base * triangle_height
            
        else:
            known_shapes = ['circle', 'rectangle', 'triangle']
            raise ValueError(f"Unsupported shape type '{shape_type}'. Supported types are {known_shapes}.")

    except (TypeError, KeyError) as e:
        # Re-raise or handle specific errors from the try block logic above which already checks validity.
        if "requires a positive numeric radius" in str(e):
            raise ValueError("Radius must be a positive number.")
        elif "Rectangle requires numeric width and height" in str(e) or \
             "Width and height must be positive numbers" in str(e):
            raise ValueError("Dimensions for rectangle must be valid positive numbers.")
        elif "Triangle requires numeric base and height" in str(e) or \
             "Base and height must be positive numbers" in str(e):
            raise ValueError("Dimensions for triangle must be valid positive numbers.")
            
    return area

if __name__ == '__main__':
    # Sample calculations to demonstrate functionality without user input
    
    shapes = [
        {
            'type': 'circle', 
            'params': {'radius': 5}
        },
        {
            'type': 'rectangle', 
            'params': {'width': 10, 'height': 4.5}
        },
        {
            'type': 'triangle', 
            'params': {'base': 8, 'height': 6}
        }
    ]

    print("Area Calculations:")
    for shape in shapes:
        result = calculate_area(shape['type'], shape['params'])
        # Format output nicely based on whether it's a whole number or float with decimals
        if isinstance(result, int):
            formatted_result = f"{result:.0f}"
        else:
            formatted_result = str(round(result, 2))
        
        print(f"Shape '{shape['type'].capitalize()}': {formatted_result}")

    # Test error handling example (commented out to ensure it doesn't run on every execution if desired, 
    # but the task says "runnable", so we can include a try-except block or just let it crash.
    # To be safe and demonstrate robustness without crashing immediately in the main output flow:
    
    print("\nError Handling Test (Circle with negative radius):")
    try:
        bad_result = calculate_area('circle', {'radius': -5})
    except ValueError as ve:
        print(f"Caught expected error: {ve}")