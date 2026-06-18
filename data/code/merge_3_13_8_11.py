def calculate_offset_difference(offsets):
    """
    Calculates the difference between the earliest and latest time zone offset.
    
    Args:
        offsets (list of int or float): A list containing numeric timezone offsets relative to UTC.
        
    Returns:
        float: The absolute difference in hours/minutes represented by the max and min offsets.
              If fewer than two valid numbers are provided, returns 0.0.
    
    Raises:
        TypeError: If any element in the list is not a number (int or float).
    """
    if len(offsets) < 2:
        return 0.0

    # Validate input types and find min/max
    try:
        numeric_offsets = [float(x) for x in offsets]
    except TypeError as e:
        raise TypeError(f"All elements must be numbers (int or float). Got invalid type.") from e
    
    max_offset = max(numeric_offsets)
    min_offset = min(numeric_offsets)

    return abs(max_offset - min_offset)

if __name__ == '__main__':
    # Hard-coded sample values representing offsets in hours/minutes relative to UTC.
    # Example: [0, 1] means UTC and UTC+1; difference is 1 hour.
    # Example: [-5, 3] means UTC-5 (e.g., EST) and UTC+3 (e.g., EET); difference is 8 hours.
    
    sample_offsets = [0, 1, -2, 4.5]

    try:
        diff = calculate_offset_difference(sample_offsets)
        
        # Output the result directly to stdout without prompts or file I/O
        print(f"The time zone offset range for {sample_offsets} is:")
        print(f"Minimum offset: {min(sample_offsets)}")
        print(f"Maximum offset: {max(sample_offsets)}")
        print(f"Difference between earliest and latest: {diff}")
    except TypeError as e:
        # Handle potential type errors gracefully during execution
        print(f"Error processing offsets: {e}")