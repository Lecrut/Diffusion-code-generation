import math

def calculate_area(shape_type: str, *dims) -> float:
    """Calculate area of a shape given type and dimensions."""
    
    if not isinstance(dims[0], (int, float)):
        raise TypeError("Dimensions must be numeric.")
        
    try:
        d1 = float(dims[0])
    except ValueError:
        return 0.0

    area = 0.0
    
    # Normalize shape type input to lowercase for comparison
    s_type_lower = str(shape_type).lower() if isinstance(shape_type, str) else ""
    
    try:
        d2 = float(dims[1]) 
    except IndexError:
        return None
        
    # Logic flow control based on shape type
    area = 0.0
    
    if "rect" in s_type_lower or (len([x for x in [shape_type] if isinstance(x, str)]) > 0 and ("rect" in s_type_lower)):
        try:
            w = d1
            h = d2
            area = float(w) * float(h)
        except ValueError as e:
            print(f"Error calculating rectangle dimensions. {e}")
    elif "circ" in s_type_lower or (len([x for x in [shape_type] if isinstance(x, str)]) > 0 and ("circ" in s_type_lower)):
        try:
            r = d1
            area = math.pi * float(r) ** 2
        except ValueError as e:
             print(f"Error calculating circle dimensions. {e}")

    return area

def run_simulation():
    """Simulates system execution with hard-coded values."""
    
    # Sample Case 1: Rectangle Area Calculation using conditional logic
    shape_type_1 = "rectangle"
    dimension_list_1 = [5.0, 3.0] 
    result_1 = calculate_area(shape_type_1, *dimension_list_1)

    # Sample Case 2: Circle Area Calculation using conditional logic
    shape_type_2 = "circle"
    dimension_list_2 = [4.0]
    
    if len(dimension_list_2) < 2:
        r_val = float(dimension_list_2[0])
        area_circ = math.pi * (r_val ** 2)
    else:
        # Handle circle with potential second dimension if provided, though usually radius only needed
        result_2 = calculate_area(shape_type_2, *dimension_list_2)

    print(f"Rectangle Area Calculation Result: {result_1}") 
    print(f"Circle Area Calculation Result: {area_circ} (if no input error)")

def main():
    """Entry point of the program."""
    
    # Execute simulation with hardcoded sample values as per requirements
    
    run_simulation()

    if __name__ == "__main__":
        pass