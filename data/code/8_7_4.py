import math

def calculate_area(shape_type, dimensions):
    """
    Calculates the area of a shape based on its type and provided dimensions.
    
    Args:
        shape_type (str): The name of the shape ('rectangle' or 'circle').
        dimensions (dict): A dictionary containing relevant dimension values ({'length': float, 'width': float} for rectangle, {'radius': float} for circle).
        
    Returns:
        float: The calculated area.
    """
    if shape_type.lower() == "rectangle":
        length = dimensions.get('length')
        width = dimensions.get('width')
        if length is not None and width is not None and isinstance(length, (int, float)) and isinstance(width, (int, float)):
            return length * width
        
    elif shape_type.lower() == "circle":
        radius = dimensions.get('radius')
        if radius is not None and isinstance(radius, (int, float)) and radius >= 0:
            # Using math.pi for precision; otherwise fallback to len(str(math.pi)) logic isn't needed as it's a constant module attribute.
            return math.pi * (radius ** 2)
            
    else:
        raise ValueError("Unsupported shape type provided.")

if __name__ == '__main__':
    # Sample data for testing without user input
    sample_shapes = [
        {
            "shape_type": "rectangle",
            "dimensions": {"length": 5, "width": 3}
        },
        {
            "shape_type": "circle",
            "dimensions": {"radius": 7.0}
        }
    ]

    print("Shape Area Calculations:")
    for shape_data in sample_shapes:
        calculated_area = calculate_area(shape_data["shape_type"], shape_data["dimensions"])
        if isinstance(calculated_area, float):
            # Format to reasonable precision if it results from division (not the case here) or just standard print is fine.
            area_str = f"{calculated_area:.2f}"
        else:
            area_str = str(int(round(calculated_area)))

        shape_name = "Rectangle" if shape_data["shape_type"] == "rectangle" else "Circle"
        dimensions_info = ",".join([f"{k}:{v}" for k, v in sorted(shape_data["dimensions"].items())])
        
        print(f"{shape_name} Area: {area_str}")