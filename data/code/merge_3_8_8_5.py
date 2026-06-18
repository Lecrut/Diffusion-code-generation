import math

def calculate_area(shape_data):
    """
    Calculates the area of a 2D shape based on parameters provided in a dictionary.
    
    Supported shapes: 'rectangle', 'circle'.
    
    Args:
        shape_data (dict): A dictionary containing the shape type and its defining parameters.
                          Expected keys depend on the shape ('shape_type').
                          
    Returns:
        float: The calculated area of the shape.
        
    Raises:
        ValueError: If an unsupported shape or invalid parameters are provided.
    """
    shape_type = shape_data.get('shape_type')

    if not isinstance(shape_type, str) or shape_type not in ['rectangle', 'circle']:
        raise ValueError(f"Unsupported shape type '{shape_type}'. Supported types: 'rectangle', 'circle'.")

    try:
        if shape_type == 'rectangle':
            width = float(shape_data['width'])
            height = float(shape_data['height'])
            
            if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                raise ValueError("Width and height must be numeric values.")

            area = width * height
            
        elif shape_type == 'circle':
            radius = float(shape_data['radius'])
            
            if not isinstance(radius, (int, float)):
                raise ValueError("Radius must be a numeric value.")

            # Ensure radius is non-negative for real area calculation
            if radius < 0:
                raise ValueError("Radius cannot be negative.")
                
            area = math.pi * (radius ** 2)
            
        else:
            return None
            
    except TypeError as e:
        raise ValueError(f"Invalid parameters provided. {e}") from e

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    samples = [
        {'shape_type': 'rectangle', 'width': 5, 'height': 10},
        {'shape_type': 'circle', 'radius': 7.5},
        {'shape_type': 'rectangle', 'width': -3, 'height': 4}, # Should raise error for negative width in logic check if strict, but math works; let's assume valid inputs only or handle gracefully based on docstring expectation of numeric input. The code raises ValueError for <0 radius specifically to ensure meaningful result.
        {'shape_type': 'triangle', 'base': 10}, # Should raise error as unsupported shape type
    ]

    print("Area Calculations:")
    for sample in samples:
        try:
            area = calculate_area(sample)
            if area is not None:
                print(f"Shape {sample['shape_type']}: Area = {area}")
            else:
                print(f"Shape {sample['shape_type']}: Error - Unhandled internal case")
        except ValueError as e:
            print(f"Error for shape {sample.get('shape_type', 'unknown')}: {e}")

    # Additional test cases to ensure robustness
    edge_cases = [
        {'shape_type': 'rectangle', 'width': 0, 'height': 5},
        {'shape_type': 'circle', 'radius': 0.1},
        {'shape_type': 'triangle', 'base': 8, 'height': None}, # Invalid parameters structure for unsupported shape too
    ]

    print("\nEdge Cases:")
    for sample in edge_cases:
        try:
            area = calculate_area(sample)
            if area is not None:
                print(f"Shape {sample['shape_type']}: Area = {area}")
            else:
                print(f"Shape {sample['shape_type']}: Error - Unhandled internal case")
        except ValueError as e:
            print(f"Error for shape {sample.get('shape_type', 'unknown')}: {e}")