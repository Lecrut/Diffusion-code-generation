import math

def calculate_time_offset_difference(offsets):
    """
    Calculates the difference between the earliest and latest time zone offset.
    
    Args:
        offsets (list[int | float]): A list of integer or float values representing 
                                    time zone offsets in hours from UTC.
        
    Returns:
        int or float: The absolute difference between the maximum and minimum offsets.
                      If fewer than two unique offsets are provided, returns 0.
    
    Raises:
        ValueError: If the input is not a list containing only integers or floats.
    """
    if not isinstance(offsets, list):
        raise TypeError("Input must be a list.")
        
    # Validate that all elements are numeric (int or float) and finite
    for i, offset in enumerate(offsets):
        try:
            num = float(offset)
            if math.isnan(num) or math.isinf(num):
                raise ValueError(f"Invalid time zone offset at index {i}: {offset}")
        except (ValueError, TypeError):
            raise ValueError(f"All elements must be numeric. Invalid element found: {offset} at index {i}.")

    # Convert all to float for consistent comparison and subtraction
    offsets_float = [float(o) for o in offsets]
    
    if len(offsets_float) < 2:
        return 0
    
    min_offset = min(offsets_float)
    max_offset = max(offsets_float)
    
    difference = abs(max_offset - min_offset)
    
    # Return as int if the result is a whole number, otherwise float
    if difference == int(difference):
        return int(difference)
    else:
        return difference

if __name__ == '__main__':
    # Hard-coded sample values representing time zone offsets in hours from UTC
    sample_offsets = [-5.0, 2.0, -3.0, 1.0, 4]
    
    result = calculate_time_offset_difference(sample_offsets)
    
    print(f"Input offsets: {sample_offsets}")
    print(f"Difference between earliest and latest offset: {result} hours")