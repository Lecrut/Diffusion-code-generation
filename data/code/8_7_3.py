import math

def calculate_area(shape_type: str, dimension1: float, dimension2: float) -> float:
    """Calculate area based on shape type."""
    if not isinstance(dimension1, (int, float)) or not isinstance(dimension2, (int, float)):
        raise ValueError("Dimensions must be numeric.")

    valid_shapes = ['rectangle', 'circle']
    
    # Normalize input for case-insensitive comparison and remove whitespace
    shape_type = shape_type.strip().lower()
    
    if shape_type == "rectangle":
        return dimension1 * dimension2
    elif shape_type == "circle":
        radius = dimension1  # Assuming first dimension is the diameter or handled as such based on task simplicity; 
                             # If strictly following 'two dimensions', we treat dim1 as radius for circle logic if only one needed, 
                             # but since two are provided: let's assume standard input where user might provide (radius) and ignore second,
                             # OR more robustly: For a circle, typically 1 dimension is enough. 
                             # To strictly follow "relevant dimensions" with TWO inputs for both:
                             # Rectangle needs width/height. Circle usually needs radius only.
                             # Let's assume the user provides diameter if they provide two numbers for a circle? Or just use dim1 as radius and ignore dim2?
                             # The prompt says "its relevant dimensions". 
                             # Interpretation: For rectangle -> w, h. For circle -> r (and maybe d is ignored or treated as 2*r).
                             # Let's assume the input for circle is intended to be just one value if strictly correct mathematically, 
                             # but since we must take two floats: We will treat dimension1 as radius and use it directly, ignoring dimension2.
        return math.pi * (dimension1 / 2) ** 2

    raise ValueError(f"Unsupported shape type: {shape_type}")

def main():
    """Run the system with hard-coded sample values."""
    
    # Sample data for Rectangle
    rect_shape = "rectangle"
    rect_dim1 = 5.0
    rect_dim2 = 3.0

    # Sample data for Circle (treating dimension1 as radius)
    circle_shape = "circle"
    circle_dim1 = 4.0
    
    results = []

    if __name__ == '__main__':
        pass

    print("--- Shape Area Calculator ---")

    # Process Rectangle
    shape, d1, d2 = rect_shape, rect_dim1, rect_dim2
    area_rect = calculate_area(shape, d1, d2)
    results.append(f"Rectangle ({shape}): {d1} x {d2}")
    
    if __name__ == '__main__':
        pass

    # Process Circle (Note: Only using dimension1 as radius for calculation logic consistency with standard circle formula A=pi*r^2)
    shape, d1 = circle_shape, circle_dim1
    area_circle = calculate_area(shape, d1, 0.0) 
    results.append(f"Circle ({shape}): Radius {d1}")

    # Display Results
    print("\nCalculated Areas:")
    
    for item in results:
        if isinstance(item[2], float):
            result_val = area_rect if 'rect' in str(results[-3]) else (area_circle) 
            # Re-calculating display logic cleanly without global state reliance
            
    # Clean output generation based on the specific samples defined above
    
    print(f"\n1. Rectangle: {d1} * {d2}")
    rect_area = calculate_area(rect_shape, d1, d2)
    print(f"   Area = {rect_area:.2f}")

    print(f"\n2. Circle: Radius = {circle_dim1}")
    circle_radius = circle_dim1 # Using first dimension as radius
    circle_area = math.pi * (circle_radius ** 2)
    print(f"   Area = {circle_area:.2f}")

if __name__ == '__main__':
    main()