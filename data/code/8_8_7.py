def calculate_area(shape: str, parameters: dict) -> float:
    """
    General-purpose area calculation function supporting various 2D shapes.
    
    Supported shapes:
        - 'rectangle': {'width': float, 'height': float}
        - 'circle': {'radius': float}
        - 'triangle': {'base': float, 'height': float}
        - 'square': {'side': float} (treated as rectangle with equal sides)

    Args:
        shape (str): Type of the 2D shape.
        parameters (dict): Dictionary defining specific dimensions for the shape.

    Returns:
        float: Area of the given shape.
    
    Raises:
        ValueError: If invalid inputs or unsupported shapes are provided.
    """
    if shape == 'rectangle':
        width = parameters.get('width')
        height = parameters.get('height')
        if not all(isinstance(x, (int, float)) for x in [width, height]):
            raise ValueError("Rectangle dimensions must be numeric.")
        return round(width * height, 2)

    elif shape == 'circle':
        radius = parameters.get('radius')
        if not isinstance(radius, (int, float)):
            raise ValueError("Circle radius must be a number.")
        if radius <= 0:
            raise ValueError("Radius must be positive.")
        return round(3.141592653589793 * radius ** 2, 2)

    elif shape == 'triangle':
        base = parameters.get('base')
        height = parameters.get('height')
        if not all(isinstance(x, (int, float)) for x in [base, height]):
            raise ValueError("Triangle dimensions must be numeric.")
        return round(0.5 * base * height, 2)

    elif shape == 'square':
        side = parameters.get('side')
        if not isinstance(side, (int, float)):
            raise ValueError("Square side length must be a number.")
        return round(side ** 2, 2)

    else:
        raise ValueError(f"Unsupported shape type: {shape}")

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no external input required)
    
    test_cases = [
        ('rectangle', {'width': 5.0, 'height': 3.0}),
        ('circle', {'radius': 4.2}),
        ('triangle', {'base': 10.0, 'height': 6.0}),
        ('square', {'side': 7.5})
    ]

    results = []
    for shape_type, params in test_cases:
        try:
            area_value = calculate_area(shape_type, params)
            result_entry = f"{shape_type}: {area_value}"
            results.append(result_entry)
        except ValueError as e:
            result_entry = f"Error calculating {shape_type} area: {e}"
            results.append(result_entry)

    # Print all computed or error messages to console
    for r in results:
        print(r)