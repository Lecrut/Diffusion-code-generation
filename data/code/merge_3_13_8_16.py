def calculate_time_zone_difference(offsets):
    """
    Calculates the difference between the earliest and latest time zone offset.
    
    Args:
        offsets (list[int | float]): A list of numeric timezone offsets relative to UTC.
        
    Returns:
        int or float: The absolute difference in hours/minutes represented by 
                     the maximum minus the minimum offset, rounded to 2 decimal places.
                     
    Raises:
        ValueError: If the input is not a non-empty list containing only numbers.
    """
    if not isinstance(offsets, list) or len(offsets) == 0:
        raise ValueError("Input must be a non-empty list of numeric offsets.")
    
    try:
        valid_offsets = [float(x) for x in offsets]
    except (ValueError, TypeError):
        raise ValueError("All elements in the list must be integers or floats.")

    min_offset = min(valid_offsets)
    max_offset = max(valid_offsets)
    
    difference = abs(max_offset - min_offset)
    
    return round(difference, 2)

if __name__ == '__main__':
    # Hard-coded sample values representing various timezone offsets (e.g., UTC-5 to UTC+3)
    sample_data = [-8.0, -4.75, 0.0, 1.66, 9.5]

    result = calculate_time_zone_difference(sample_data)

    # Output the calculated difference for verification purposes (no user input required)
    print(f"Timezone offset range: {min(sample_data)} to {max(sample_data)}")
    print(f"Difference in hours/minutes units: {result}")