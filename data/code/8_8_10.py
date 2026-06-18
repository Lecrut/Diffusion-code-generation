def calculate_area(shape_data: dict) -> float:
    """
    Calculate the area of a 2D shape based on dictionary parameters.
    
    Supported shapes: 'circle', 'rectangle', 'triangle'
    
    Args:
        shape_data (dict): Dictionary containing 'shape_type' and relevant dimensions
        
    Returns:
        float: The calculated area
    
    Raises:
        ValueError: If invalid shape type or missing required parameters
    """
    shape_type = shape_data.get('shape_type')
    
    if not isinstance(shape_type, str) or shape_type == '':
        raise ValueError("Shape type must be a non-empty string")
    
    area_map = {
        'circle': calculate_circle_area,
        'rectangle': calculate_rectangle_area,
        'triangle': calculate_triangle_area
    }
    
    if shape_type not in area_map:
        raise ValueError(f"Unsupported shape type '{shape_type}'. Supported types are circle, rectangle, triangle")
    
    return area_map[shape_type](shape_data)

def calculate_circle_area(data: dict) -> float:
    """Calculate the area of a circle."""
    radius = data.get('radius')
    if not isinstance(radius, (int, float)):
        raise ValueError("Circle requires a valid numeric radius")
    return 3.141592653589793 * radius ** 2

def calculate_rectangle_area(data: dict) -> float:
    """Calculate the area of a rectangle."""
    width = data.get('width')
    height = data.get('height')
    
    if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Rectangle requires valid numeric width and height")
        
    return abs(width) * abs(height)

def calculate_triangle_area(data: dict) -> float:
    """Calculate the area of a triangle."""
    base = data.get('base')
    height = data.get('height')
    
    if not isinstance(base, (int, float)) or not isinstance(height, (int, float)):
        raise ValueError("Triangle requires valid numeric base and height")
        
    return 0.5 * abs(base) * abs(height)

if __name__ == '__main__':
    # Sample calculations without user input
    
    samples = [
        {
            'description': 'Circle with radius 5',
            'data': {'shape_type': 'circle', 'radius': 5}
        },
        {
            'description': 'Rectangle width 4 height 6',
            'data': {'shape_type': 'rectangle', 'width': 4, 'height': 6}
        },
        {
            'description': 'Triangle base 10 height 3',
            'data': {'shape_type': 'triangle', 'base': 10, 'height': 3}
        }
    ]
    
    print("Area Calculations:\n")
    
    for sample in samples:
        try:
            area = calculate_area(sample['data'])
            description = f"{sample['description']}: {area:.2f}"
            print(description)
            
            # Additional test case with floating point values
            float_test_data = {'shape_type': 'rectangle', 'width': 3.5, 'height': 7.2}
            area_float = calculate_area(float_test_data)
            print(f"Float rectangle (3.5 x 7.2): {area_float:.4f}")
            
        except ValueError as e:
            description = f"{sample['description']} -> Error: {e}"
            print(description)