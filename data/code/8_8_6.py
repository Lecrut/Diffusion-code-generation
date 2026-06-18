"""General-purpose area calculation function for various 2D shapes."""

def calculate_area(shape_type: str, parameters: dict) -> float:
    """
    Calculate the area of a 2D shape based on its type and defining parameters.

    Supported shapes:
        - 'rectangle': requires {'width', 'height'}
        - 'circle': requires {'radius'}
        - 'triangle': requires {'base', 'height'}
    
    Args:
        shape_type (str): Type of the shape ('rectangle', 'circle', or 'triangle').
        parameters (dict): Dictionary containing defining parameters for the shape.

    Returns:
        float: The calculated area of the shape.

    Raises:
        ValueError: If an unsupported shape type is provided or required parameters are missing/invalid.
    """
    
    if not isinstance(shape_type, str) or shape_type.lower() == '':
        raise ValueError("Shape type must be a non-empty string.")
    
    valid_shapes = ['rectangle', 'circle', 'triangle']
    if shape_type.lower() not in valid_shapes:
        raise ValueError(f"Unsupported shape type '{shape_type}'. Supported types are {valid_shapes}.")

    params_lower_key = shape_type.lower()
    required_params_map = {
        'rectangle': {'width', 'height'},
        'circle': {'radius'},
        'triangle': {'base', 'height'}
    }
    
    if not isinstance(parameters, dict):
        raise ValueError("Parameters must be a dictionary.")

    missing_keys = required_params_map[params_lower_key] - set(parameters.keys())
    if missing_keys:
        raise ValueError(f"Missing required parameters for '{shape_type}': {missing_keys}.")

    try:
        width = float(parameters['width']) if 'width' in parameters else 0.0
        height = float(parameters['height']) if 'height' in parameters else 0.0
        radius = float(parameters['radius']) if 'radius' in parameters else 0.0
        base = float(parameters['base']) if 'base' in parameters else 0.0
        
        # Validate non-negative dimensions for geometric sense (optional but recommended)
        if width < 0 or height < 0:
            raise ValueError("Width and height must be non-negative.")
        if radius < 0:
            raise ValueError("Radius must be non-negative.")
        if base < 0:
            raise ValueError("Base must be non-negative.")

    except (TypeError, KeyError):
        # Re-raise as a more specific error or handle type conversion failure
        raise TypeError(f"Parameters for '{shape_type}' must contain valid numeric values.") from None
    
    area = 0.0
    
    if params_lower_key == 'rectangle':
        area = width * height
    elif params_lower_key == 'circle':
        import math
        area = math.pi * (radius ** 2)
    elif params_lower_key == 'triangle':
        area = 0.5 * base * height
    
    return area

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or files.

    samples = [
        {
            "shape_type": "rectangle",
            "parameters": {"width": 10, "height": 5}
        },
        {
            "shape_type": "circle",
            "parameters": {"radius": 7}
        },
        {
            "shape_type": "triangle",
            "parameters": {"base": 8, "height": 4.5}
        }
    ]

    print("Area Calculation Results:")
    for sample in samples:
        try:
            result = calculate_area(sample["shape_type"], sample["parameters"])
            shape_name = sample["shape_type"].capitalize()
            params_str = f"{', '.join([f'{k}={v}' if isinstance(v, int) else str(f'{v}') for k, v in sorted(sample['parameters'].items(), key=lambda x: (isinstance(x[1], float), x[0]))])}"
            
            print(f"Shape: {shape_name}")
            print(f"Parameters: {params_str}")
            print(f"Area: {result:.2f}\n")
        except Exception as e:
            print(f"Error calculating area for sample '{sample['shape_type']}': {e}\n")

    # Additional test case with invalid input to demonstrate error handling
    try:
        calculate_area("pentagon", {"sides": 5})
    except ValueError as ve:
        print(f"Expected Error Handling Test:")
        print(f"Input: {{'shape_type': 'pentagon', 'parameters': {{'sides': 5}}}}")
        print(f"Error Message: {ve}\n")