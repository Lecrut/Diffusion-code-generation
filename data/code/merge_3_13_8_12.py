def calculate_offset_difference(offsets):
    """
    Calculates the difference between the earliest and latest time zone offset.
    
    Args:
        offsets (list[int | float]): A list of integer or float values representing 
                                    time zone offsets from UTC.
        
    Returns:
        int or float: The absolute difference between the maximum and minimum offsets.
                      If the input is empty, returns 0.
                      
    Raises:
        TypeError: If any element in the list is not an instance of int or float.
        ValueError: If the input is not a list.
    """
    if not isinstance(offsets, list):
        raise ValueError("Input must be a list.")
    
    for offset in offsets:
        if not (isinstance(offset, (int, float)) and not isinstance(offset, bool)):
            raise TypeError(f"All elements must be integers or floats. Found {type(offset).__name__}.")

    if len(offsets) == 0:
        return 0
    
    max_offset = max(offsets)
    min_offset = min(offsets)
    
    difference = abs(max_offset - min_offset)
    return difference

if __name__ == '__main__':
    # Hard-coded sample values representing time zone offsets from UTC
    sample_offsets = [-120, 60, 350.5, -480]
    
    result = calculate_offset_difference(sample_offsets)
    print(f"The difference between the earliest and latest offset is: {result}")