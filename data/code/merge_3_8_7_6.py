import math

def calculate_area(shape: str, dimension1: float, dimension2: float) -> None:
    """Calculate area based on shape type using conditional logic."""
    
    # Normalize shape input to lowercase and remove whitespace
    normalized_shape = shape.strip().lower()
    
    if not (normalized_shape == "rectangle" or normalized_shape == "circle"):
        print(f"Error: Invalid shape '{shape}'. Please use 'rectangle' or 'circle'.")
        return

    area = 0.0
    
    try:
        if dimension1 <= 0 or dimension2 <= 0:
            raise ValueError("Dimensions must be positive numbers.")
        
        if normalized_shape == "rectangle":
            # Area of rectangle = length * width
            area = dimension1 * dimension2
            
        elif normalized_shape == "circle":
            # For a circle, we assume the input is diameter. 
            # If intended as radius, it would require different logic or user prompt (avoided per constraints).
            # Here we treat both inputs as if they represent equivalent linear dimensions for calculation context,
            # but strictly following 'dimension1' and 'dimension2', a circle typically uses one value (radius/diameter).
            # To satisfy the function signature requiring two parameters while handling circles:
            # We interpret dimension1 as diameter. dimension2 is ignored or used to represent radius if specified differently.
            # However, adhering strictly to "relevant dimensions" for a circle usually implies just one number.
            # Given the constraint of passing 'dimension2', we will assume the user passed two numbers 
            # but only needs one for calculation (e.g., diameter). We'll use dimension1 as diameter and ignore dim2 with a warning,
            # OR if the intention is radius provided twice or similar:
            # Let's implement standard circle area = pi * r^2. If input was meant to be 'diameter', we divide by 2 first.
            # To keep it robust without prompts: We will assume dimension1 is diameter and use it. 
            # Note: In a real scenario, the prompt would ask for radius or diameter explicitly.
            
            if normalized_shape == "circle":
                # Assuming 'dimension1' represents the Diameter based on common input patterns where two params are given loosely.
                # If the user intended Radius as dimension2 and Diameter ignored? Unlikely. 
                # Let's assume standard case: Input is Diameter (dim1). 
                diameter = dimension1
                radius = diameter / 2.0
                area = math.pi * (radius ** 2)

    except ValueError as ve:
        print(f"Error: {ve}")
        return
    
    # Display result
    if normalized_shape == "rectangle":
        unit_text = ""
        print(f"\nShape: Rectangle")
        print(f"Dims: {dimension1} x {dimension2}")
        print(f"Area: {area:.4f}{unit_text}")
    else:
        unit_text = "" # Assuming no specific units requested in prompt context beyond calculation
        print(f"\nShape: Circle")
        print(f"Diameter (used): {diameter}")
        print(f"Radius used: {radius}")
        print(f"Area: {area:.4f}{unit_text}")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements. 
    # No user input, args, or network access is required for this block to run.

    test_cases = [
        ("rectangle", 5, 10),       # Rectangle: length=5, width=10
        ("circle", 20, None),      # Circle: diameter=20 (dimension2 ignored as circle typically needs one linear dim)
        ("invalid_shape", 3, 4),   # Invalid shape to test error handling logic flow
    ]

    for i, case in enumerate(test_cases):
        print(f"\n--- Test Case {i+1} ---")
        
        if len(case) == 2:
            shape = case[0]
            d1 = case[1]
            # Handle circle specifically where second param might be None or ignored logic applied inside function
            calculate_area(shape, d1, d1 * 2) 
        else:
            print(f"Skipping test with insufficient data.")

    # Explicit clean run for the primary requirement demonstration without complex list overhead if desired:
    print("\n--- Primary Demonstration Run ---")
    
    # Sample values as requested (no external input)
    shape_demo = "rectangle"
    dim1_demo = 8.5
    dim2_demo = 4.0
    
    calculate_area(shape_demo, dim1_demo, dim2_demo)

    print("\n--- Secondary Circle Demonstration ---")
    
    # Sample circle values (treating first as diameter per logic above to utilize two args safely or just passing one relevant and second arbitrary positive)
    shape_circle = "circle"
    d_dim1 = 7.0
    
    calculate_area(shape_circle, d_dim1, d_dim1 + 2)