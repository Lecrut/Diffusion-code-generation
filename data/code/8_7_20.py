import math

def calculate_area(shape_type: str, dimension1: float, dimension2: float) -> float:
    """Calculates the area of a shape based on type and dimensions."""
    if shape_type.lower() == "rectangle":
        return dimension1 * dimension2
    elif shape_type.lower() == "circle":
        # Assuming radius is provided as dimension1 for circle, 
        # or we could treat one input as diameter. Here treating first dim as radius.
        return math.pi * (dimension1 ** 2)
    else:
        raise ValueError(f"Unsupported shape type: {shape_type}")

def get_shape_input() -> tuple[str, float]:
    """Simulates user interaction by returning hard-coded values."""
    # Hardcoded sample inputs to avoid interactive prompts
    return "rectangle", 5.0

if __name__ == '__main__':
    shape_input = None
    
    # Simulate logic for different shapes with hardcoded data
    test_cases = [
        ("rectangle", 10, 20),
        ("circle", 7),
        ("triangle", "unsupported"), # This will trigger the else block to demonstrate error handling if needed, 
                                    # but based on task requirements we only support rect/circle.
    ]

    for shape_type, dim_a in test_cases:
        try:
            area = calculate_area(shape_type, dim_a)
            print(f"Shape: {shape_type}")
            print(f"Dimension(s): {dim_a}x{dim_a if 'circle' not in shape_type else ''}") # Simplified display for demo
            print(f"Calculated Area: {area:.2f}\n")
        except ValueError as e:
            print(f"Error processing input: {e}\n")

    # Explicit single run example matching the prompt's implied simplicity
    sample_shape, sample_dim = get_shape_input()
    
    if sample_shape.lower() == "rectangle":
        area_result = calculate_area(sample_shape, sample_dim, 10.5)
        print(f"Rectangle Area: {area_result}")
    elif sample_shape.lower() == "circle":
        # Adjusting logic for the specific single run example to ensure valid inputs if passed via function call above
        # The get_shape_input returns ('rectangle', 5.0), so we use that directly or simulate a circle case below:
        pass

    # Additional explicit demonstration of Circle calculation as per task requirements (Rectangle/Circle)
    sample_circle_dim = 3.14
    if "circle" in str(sample_cases := [("circle", sample_circle_dim)]): 
        area_result_circle = calculate_area("circle", sample_circle_dim, None)
        print(f"Circle Area: {area_result_circle:.2f}")

    # Final consolidated output based on the initial get_shape_input call which is 'rectangle' 5.0
    final_shape, final_dim1 = "rectangle", 6.0
    if final_shape.lower() == "rectangle":
        area_final = calculate_area(final_shape, final_dim1, 4.0)
        print(f"Final Rectangle Area (dim: {final_dim1}, height: 4): {area_final}")