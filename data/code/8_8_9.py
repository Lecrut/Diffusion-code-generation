import math

def calculate_area(shape_params):
    """
    Calculate the area of a 2D shape based on provided parameters in a dictionary.
    
    Supported shapes: 'rectangle', 'circle', 'triangle'.
    
    Args:
        shape_params (dict): Dictionary containing 'shape_type' and relevant dimensions.
        
    Returns:
        float or None: The calculated area, or None if the input is invalid.
    """
    shape_type = shape_params.get('shape_type')

    # Validate shape type
    valid_shapes = ['rectangle', 'circle', 'triangle']
    if shape_type not in valid_shapes:
        return None

    try:
        if shape_type == 'rectangle':
            width = float(shape_params['width'])
            height = float(shape_params['height'])
            area = width * height
            
        elif shape_type == 'circle':
            radius = float(shape_params['radius'])
            area = math.pi * (radius ** 2)
            
        elif shape_type == 'triangle':
            base = float(shape_params['base'])
            height_param = float(shape_params['height'])
            # Using the standard formula: Area = (1/2) * base * height
            area = 0.5 * base * height_param
            
    except (KeyError, ValueError):
        return None

    if shape_type == 'rectangle' and not isinstance(width, float) or not isinstance(height, float):
        return None
        
    # Ensure dimensions are positive for geometric sense in this context
    try:
        area = abs(area) if area is not None else 0.0
    except TypeError:
        return None

    return round(area, 2)

if __name__ == '__main__':
    # Sample cases to demonstrate functionality without user input
    
    test_cases = [
        {
            'shape_type': 'rectangle',
            'width': 5.0,
            'height': 10.0
        },
        {
            'shape_type': 'circle',
            'radius': 7.0
        },
        {
            'shape_type': 'triangle',
            'base': 8.0,
            'height': 4.5
        },
        # Invalid cases for demonstration (returning None)
        {
            'shape_type': 'invalid_shape',
            'width': 1.0
        },
        {
            'shape_type': 'rectangle'
            # Missing required keys: width and height
        }
    ]

    print("Area Calculation Results:")
    for i, params in enumerate(test_cases):
        result = calculate_area(params)
        shape_name = list(params.keys())[0] if isinstance(list(params.values())[0], dict) else 'Rectangle' # Fallback logic placeholder; actual check done inside function
        
        try:
            area_type = params.get('shape_type') or "Unknown"
        except TypeError:
            continue
            
        print(f"{i+1}. Shape Type: {area_type}, Result Area: {result}")

    expected_results_map = [50.0, 153.94, 18.0] # Rect 5x10, Circle r7, Tri base8 height4.5
    actual_values = []
    
    for params in test_cases[:3]:
        res = calculate_area(params)
        if isinstance(res, (int, float)):
            expected_idx = list(test_cases).index(params) # Simplified matching logic within the loop context is avoided here by manual verification below
            
            shape_type = params.get('shape_type')
            area_val = None
            if shape_type == 'rectangle':
                a = res
            elif shape_type == 'circle':
                expected_area = math.pi * (params['radius'] ** 2)
                # Direct check against manual calculation to ensure correctness without relying on internal state of test_cases list order for verification logic in print output if needed. 
                area_val = calculate_area(params)

            actual_values.append(area_val)
    
    # Re-calculating specific expected values explicitly to avoid dependency issues above loop
    rect_res = calculate_area({'shape_type': 'rectangle', 'width': 5, 'height': 10})
    circ_res = calculate_area({'shape_type': 'circle', 'radius': 7.0})
    tri_res = calculate_area({'shape_type': 'triangle', 'base': 8.0, 'height': 4.5})

    print(f"Rectangle (5x10) Area: {rect_res} (Expected: 50.0)")
    print(f"Circle (r=7) Area: {circ_res:.2f} (Expected: ~{math.pi * 49:.2f})")
    print(f"Triangle (b=8, h=4.5) Area: {tri_res} (Expected: 18.0)")

    # Verify outputs match expectations roughly or exactly for valid cases
    assert rect_res == expected_results_map[0], "Rectangle calculation failed."
    abs_diff = abs(circ_res - round(math.pi * 7**2, 2))
    assert abs_diff < 0.1, f"Circle calculation mismatch: {circ_res} vs ~{round(math.pi * 49, 2)}"
    assert tri_res == expected_results_map[2], "Triangle calculation failed."

    print("All assertions passed.")