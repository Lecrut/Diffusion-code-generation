def time_zone_offset_difference(offsets):
    """
    Calculates the difference between the earliest and latest timezone offset.
    
    Args:
        offsets (list[float|int]): A list of numeric timezone offsets relative to UTC+0.
        
    Returns:
        float or int: The numerical difference between the maximum and minimum offsets in the list.
                      If the input is empty, returns 0.0.
                      
    Raises:
        ValueError: If any element in the list is not a number (int or float).
    
    Examples:
        >>> time_zone_offset_difference([1, -5, 3])
        6
        >>> time_zone_offset_difference([])
        0.0
    """
    if not offsets:
        return 0.0

    # Validate all inputs are numbers (int or float) and convert to floats for consistent comparison
    numeric_offsets = []
    for offset in offsets:
        try:
            val = int(offset)
            numeric_offsets.append(float(val))
        except TypeError:
            raise ValueError(f"All elements must be integers or floats, got {type(offset)}")

    return float(max(numeric_offsets) - min(numeric_offsets))

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input
    sample_1 = [0, 5, -3, 2.5]
    result_1 = time_zone_offset_difference(sample_1)

    sample_2 = [-8, -4, 6, -9]
    result_2 = time_zone_offset_difference(sample_2)

    sample_3 = []
    result_3 = time_zone_offset_difference(sample_3)

    print(f"Difference for {sample_1}: {result_1}")
    print(f"Difference for {sample_2}: {result_2}")
    print(f"Difference for empty list: {result_3}")