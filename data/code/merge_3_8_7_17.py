def calculate_area(shape_type: str, dimension1: float, dimension2: float) -> float:
    """Calculate area based on shape type and dimensions."""
    if shape_type.lower() == "rectangle":
        return dimension1 * dimension2
    elif shape_type.lower() == "circle":
        # Assuming the second input is diameter for simplicity in this context.
        radius = dimension2 / 2
        import math
        return math.pi * (radius ** 2)
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

if __name__ == '__main__':
    # Hard-coded sample values to run without user input or command-line arguments.

    # Sample Case 1: Rectangle with width=5 and height=3
    rect_shape = "rectangle"
    rect_dim1 = 5.0
    rect_dim2 = 3.0
    
    area_rect = calculate_area(rect_shape, rect_dim1, rect_dim2)
    
    print(f"Shape: {rect_shape}")
    print(f"Dimensions: {rect_dim1} x {rect_dim2}")
    print(f"Calculated Area: {area_rect:.2f}\n")

    # Sample Case 2: Circle with diameter=6 (radius will be derived)
    circle_shape = "circle"
    circle_diameter = 6.0
    
    area_circle = calculate_area(circle_shape, 1.0, circle_diameter) # dimension1 is unused for calculation logic but required by function signature

    print(f"Shape: {circle_shape}")
    print(f"Diameter: {circle_diameter}")
    print(f"Calculated Area: {area_circle:.2f}")