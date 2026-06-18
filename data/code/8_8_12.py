"""
General-purpose area calculation function for various 2D shapes.
Accepts a dictionary specifying the shape type and its defining parameters.
Supports: 'circle', 'rectangle', 'triangle' (right-angled), 'polygon'.
For polygon, vertices are expected as a list of [x, y] tuples in counter-clockwise order.

No user input, command-line arguments, or network access is used.
"""

def calculate_area(shape_data):
    """
    Calculate the area of a 2D shape based on provided parameters.
    
    Args:
        shape_data (dict): Dictionary containing 'type' and relevant parameters.
            Supported types:
                - 'circle': {'radius': float} or {'diameter': float}
                - 'rectangle': {'width': float, 'height': float}
                - 'triangle': {'base': float, 'height': float} (right-angled)
                - 'polygon': {'vertices': list of [x, y] tuples}

    Returns:
        float: The calculated area.

    Raises:
        ValueError: If the shape type is unsupported or parameters are invalid.
    """
    
    shape_type = shape_data.get('type')
    
    if not isinstance(shape_type, str):
        raise ValueError("Shape 'type' must be a string.")
        
    valid_types = ['circle', 'rectangle', 'triangle', 'polygon']
    if shape_type not in valid_types:
        raise ValueError(f"Unsupported shape type. Must be one of {valid_types}.")

    try:
        if shape_type == 'circle':
            radius_data = shape_data.get('radius') or shape_data.get('diameter')
            if radius_data is None:
                raise ValueError("Circle must have either 'radius' or 'diameter'.")
            
            r = radius_data / 2.0 if isinstance(radius_data, (int, float)) else radius_data ** 0.5
            
            return round(r * r * 3.141592653589793, 2)

        elif shape_type == 'rectangle':
            width = shape_data.get('width')
            height = shape_data.get('height')
            
            if not isinstance(width, (int, float)) or not isinstance(height, (int, float)):
                raise ValueError("Rectangle must have numeric 'width' and 'height'.")
                
            return round(abs(width) * abs(height), 2)

        elif shape_type == 'triangle':
            base = shape_data.get('base')
            height_param = shape_data.get('height')
            
            if not isinstance(base, (int, float)) or not isinstance(height_param, (int, float)):
                raise ValueError("Triangle must have numeric 'base' and 'height'.")
                
            return round(abs(base) * abs(height_param) / 2.0, 2)

        elif shape_type == 'polygon':
            vertices = shape_data.get('vertices')
            
            if not isinstance(vertices, list):
                raise ValueError("Polygon must have a list of 'vertices'.")
                
            for v in vertices:
                if not isinstance(v, (list, tuple)) or len(v) != 2:
                    raise ValueError("Each vertex must be a [x, y] pair.")

            area = 0.5 * abs(sum(vertices[i][0]*vertices[(i+1)%len(vertices)][1] - 
                                   vertices[i][1]*vertices[(i+1)%len(vertices)][0] for i in range(len(vertices))))
            
            return round(area, 2)

        else:
            raise ValueError(f"Shape type '{shape_type}' not implemented.")

    except Exception as e:
        if isinstance(e, TypeError):
            raise ValueError("Invalid parameter types provided for the shape calculation.") from None
        elif isinstance(e, KeyError):
            raise ValueError(f"Missing required parameters for {shape_type}.") from None
        else:
            raise

if __name__ == '__main__':
    # Sample test cases with hard-coded values (no user input or files)

    samples = [
        {'type': 'circle', 'radius': 5},
        {'type': 'rectangle', 'width': 10, 'height': 7.5},
        {'type': 'triangle', 'base': 8, 'height': 4},
        {'type': 'polygon', 'vertices': [[0, 0], [2, 3], [-1, 1]]}
    ]

    print("Area Calculations:")
    for shape_data in samples:
        try:
            area = calculate_area(shape_data)
            # Extract type name safely without relying on input() or args
            result_str = f"{shape_data['type']} Area: {area}"
            print(result_str)
        except Exception as e:
            error_msg = str(e).replace("Invalid parameter types provided for the shape calculation.", "")
            if "Missing required parameters" in error_msg:
                missing_key = list(shape_data.keys())[0] # Fallback logic, though specific keys are known
                print(f"{shape_data['type']} Error: {error_msg}")
            else:
                print(f"{shape_data['type']} Error: {e}")

    # Additional edge case test for diameter input instead of radius
    extra_samples = [
        {'type': 'circle', 'diameter': 10},
        {'type': 'rectangle', 'width': -5, 'height': 3} # Negative dimensions handled by abs logic in original thought process but let's ensure robustness. The prompt says "valid parameters". Let's assume positive for geometry usually, but mathematically area is magnitude.*magnitude. I will stick to absolute values as per standard geometric definition unless specified otherwise.
    ]

    print("\nAdditional Tests:")
    for shape_data in extra_samples:
        try:
            area = calculate_area(shape_data)
            result_str = f"{shape_data['type']} Area: {area}"
            print(result_str)
        except Exception as e:
            error_msg = str(e).replace("Invalid parameter types provided for the shape calculation.", "")
            if "Missing required parameters" in error_msg:
                missing_key = list(shape_data.keys())[0] 
                print(f"{shape_data['type']} Error: {error_msg}")
            else:
                print(f"{shape_data['type']} Error: {e}")