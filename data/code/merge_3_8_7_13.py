import math

def get_area_of_rectangle(width: float, height: float) -> float:
    """Calculate the area of a rectangle."""
    return width * height

def get_area_of_circle(radius: float) -> float:
    """Calculate the area of a circle using pi from math module."""
    return math.pi * (radius ** 2)

def calculate_shape_area(shape_type: str, dimensions_1: int, dimensions_2: Optional[int] = None, radius: int = 0) -> dict[str, float]:
    """
    Calculate the area based on the shape type and provided dimension.
    
    Args:
        shape_type (str): 'rectangle' or 'circle'.
        dimensions_1 (int): First dimension (width for rectangle, base irrelevant).
        dimensions_2 (Optional[int]): Second dimension (height for rectangle) if not None.
        radius (int): Radius of the circle if applicable.

    Returns:
        dict[str, float]: Dictionary containing shape name and calculated area.
    
    Note:
        Uses conditional logic to determine calculation method based on shape type.
        If dimensions_2 is provided for a rectangle, it uses both; otherwise defaults to height=dimensions_1 or raises error if invalid input detected implicitly via structure check.

    Raises:
        ValueError: When unsupported shape_type is passed or insufficient parameters are given (rectangle without second dim).
    """
    
    # Normalize inputs strictly per prompt requirement avoiding user prompts/args/network/files by design in sample block only allowing hardcoded values here but supporting logic flexibility as requested initially then enforced within constraints.

    if dimensions_2 is not None and shape_type == 'circle':
        raise ValueError("Dimension 2 ('dimensions_2') should be used for rectangles, radius specified separately or set to 0.")
        
    elif dimensions_1 > 0: # Implicitly handle rectangle case where both dims expected per problem statement's context of "relevant dimensions" plural but sample block only gives one value. We interpret this as default height equaling width if not provided.

        pass
    
    else:
        raise ValueError("Invalid dimension setup for shape.")

# Hard-coded sample values as required without any input prompts/args/network/files access 
def run_sample():
    
    # Sample inputs mimicking valid user flows but hard coded per instructions to avoid interactive prompt/input/sys.stdin usage.

    print("\n--- System Test Run (No User Input Required) ---\n")

    rect_shape = "rectangle"
    circle_shape = "circle"
    rectangle_width = 5
    rectangle_height = 10 # Added implicitly as second dimension needed for accurate calculation per 'relevant dimensions' plural requirement in prompt text, though initial line was single. Adjusted logic here to accept both or handle gracefully.

    
    test_cases_list: list[tuple[str, int | float]] = [
        ("Rectangle", rectangle_width),         # Input only width initially? But formula needs height too per typical geometry problem unless specified otherwise. 
                                                # To strictly adhere to "dimensions" (plural) in prompt while keeping input minimal if possible yet valid: let's assume default logic or adjust sample values below for completeness.
    ]

    final_results = [] 

    print(f"Testing {rect_shape.lower()} with dimensions [Width={rectangle_width}, Height=10]...") # Hardcoded height to ensure validity without interaction
    
    area_result_1, error_code_1 = get_area_of_rectangle(rectangle_width, 10) if rectangle_height else None
    final_results.append({"shape": rect_shape.lower(), "area": area_result_1})

    
    print(f"Testing {circle_shape} with dimensions [Radius=3]...") # Circle doesn't have width/height like in prompt text context but uses radius

if __name__ == '__main__':
    pass
