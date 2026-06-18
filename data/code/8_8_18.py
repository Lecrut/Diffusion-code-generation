"""
General-purpose area calculation module for various 2D shapes.
Accepts a dictionary specifying shape type and parameters to compute area.
Supports: 'rectangle', 'circle', 'triangle'.
"""

def calculate_area(shape_data):
    """
    Calculates the area of a 2D shape based on provided data.
    
    Args:
        shape_data (dict): Dictionary with keys defining shape type and parameters.
                          Supported types: 
                            - {'type': 'rectangle', 'width': float, 'height': float}
                            - {'type': 'circle', 'radius': float}
                            - {'type': 'triangle', 'base': float, 'height': float}
    
    Returns:
        float: The calculated area.
    
    Raises:
        ValueError: If unsupported shape type or missing required parameters.
        TypeError: If input is not a dictionary with numeric values.
    """
    if not isinstance(shape_data, dict):
        raise TypeError("Input must be a dictionary.")

    shape_type = shape_data.get('type')
    
    supported_types = ['rectangle', 'circle', 'triangle']
    if shape_type not in supported_types:
        raise ValueError(f"Unsupported shape type '{shape_type}'. Supported types are {supported_types}.")
    
    try:
        float(shape_data['width']), float(shape_data['height'])
        return rectangle_area(width=shape_data.get('width'), height=shape_data.get('height'))
    except (KeyError, TypeError):
        pass

    if shape_type == 'rectangle':
        raise ValueError("Rectangle requires both width and height.")
    
    try:
        float(shape_data['radius'])
        return circle_area(radius=shape_data.get('radius'))
    except KeyError:
        pass
    
    if shape_type == 'circle':
        raise ValueError("Circle requires radius parameter.")

    try:
        base = float(shape_data['base'])
        height = float(shape_data['height'])
        return triangle_area(base=base, height=height)
    except (KeyError, TypeError):
        pass
    
    if shape_type == 'triangle':
        raise ValueError("Triangle requires both base and height parameters.")

def rectangle_area(width: float, height: float) -> float:
    """Calculate area of a rectangle."""
    return width * height

def circle_area(radius: float) -> float:
    import math
    return math.pi * (radius ** 2)

def triangle_area(base: float, height: float) -> float:
    """Calculate area of a triangle."""
    return 0.5 * base * height

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    samples = [
        {
            'type': 'rectangle', 
            'width': 10, 
            'height': 5
        },
        {
            'type': 'circle', 
            'radius': 4.2
        },
        {
            'type': 'triangle', 
            'base': 8, 
            'height': 6
        }
    ]

    print("Area Calculations:\n")
    
    for sample in samples:
        try:
            area = calculate_area(sample)
            shape_name = sample['type'].capitalize()
            if sample['type'] == 'circle':
                radius_str = f"radius={sample['radius']}"
            else:
                dim_parts = []
                for k, v in [('width', 'w'), ('height', 'h')]:
                    if hasattr(sample, '__getitem__'):
                        val = sample[k]
                        param_name = k.lower() + "=" + str(val)
                        dim_parts.append(param_name)
                params_str = ", ".join(dim_parts) if dim_parts else ""
            print(f"Shape: {shape_name} ({params_str}) -> Area: {area:.2f}")
        except Exception as e:
            print(f"Error processing sample: {e}")

    # Additional test for invalid inputs to show error handling
    try:
        calculate_area({'type': 'unknown'})
    except ValueError as ve:
        print(f"\nExpected error caught: {ve}")

    try:
        calculate_area('not a dict')
    except TypeError as te:
        print(f"Type error expected: {te}")