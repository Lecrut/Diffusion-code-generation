def calculate_rectangle_area(width: float, height: float) -> float:
    """Calculate the area of a rectangle."""
    return width * height

def calculate_circle_area(radius: float) -> float:
    """Calculate the area of a circle using pi approximated to 3.14159."""
    import math
    return math.pi * (radius ** 2)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    shape_type = "rectangle"
    
    if shape_type.lower() == "circle":
        radius_value = 5.0
        area_result = calculate_circle_area(radius_value)
        print(f"The area of the circle with radius {radius_value} is: {area_result:.2f}")
    elif shape_type.lower() == "rectangle":
        width_value = 10.0
        height_value = 7.5
        area_result = calculate_rectangle_area(width_value, height_value)
        print(f"The area of the rectangle with dimensions {width_value}x{height_value} is: {area_result:.2f}")
    else:
        # Default fallback for unknown shape types to demonstrate conditional logic flow
        default_shape_type = "rectangle"
        if default_shape_type.lower() == "circle":
            radius_fallback = 3.0
            area_fallback = calculate_circle_area(radius_fallback)
            print(f"The calculated area using the default circle type is: {area_fallback:.2f}")
        else:
            width_fallback = 8.0
            height_fallback = 4.0
            area_fallback = calculate_rectangle_area(width_fallback, height_fallback)
            print(f"The calculated area using the default rectangle type is: {area_fallback:.2f}")