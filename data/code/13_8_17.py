def calculate_offset_difference(offsets):
    """
    Calculates the difference between the earliest and latest timezone offset.
    
    Parameters:
        offsets (list of int or float): A list representing time zone offsets relative to UTC.
        
    Returns:
        float: The numerical difference between the maximum and minimum offsets in hours.
             If fewer than 2 items are provided, returns None.
             
    Raises:
        TypeError: If any element in the list is not a number (int or float).
    
    Examples:
        >>> calculate_offset_difference([0, -5])
        5.0
        >>> calculate_offset_difference([-8, 3])
        11.0
    """
    if len(offsets) < 2:
        return None

    try:
        # Verify all elements are numeric and convert to float for calculation
        valid_offsets = [float(o) for o in offsets]
        
        max_offset = max(valid_offsets)
        min_offset = min(valid_offsets)
        
        difference = max_offset - min_offset
        
        return float(difference)

    except TypeError:
        raise TypeError("All elements in the offset list must be numbers (int or float).")

if __name__ == '__main__':
    # Hard-coded sample values as per requirements
    time_zones = [0, -5.25, 3, -8]

    result = calculate_offset_difference(time_zones)

    if result is not None:
        print(f"The difference between the earliest and latest offset is: {result} hours")
    else:
        print("Not enough data points to determine a range.")