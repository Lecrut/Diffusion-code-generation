def calculate_offset_difference(offsets):
    """
    Calculates the difference between the earliest and latest time zone offset.
    
    Parameters:
        offsets (list[int | float]): A list of numeric timezone offsets relative to UTC.
        
    Returns:
        int or float: The absolute difference in hours/minutes represented by 
                     the maximum minus minimum value in the input list.
                     
    Raises:
        ValueError: If the input is not a non-empty list containing only numbers.
        TypeError: If any element in the list cannot be converted to a number (int or float).
    
    Examples:
        >>> calculate_offset_difference([0, 5, -3])
        8
        >>> calculate_offset_difference([-2, -1, 4])
        6.0
    """
    if not isinstance(offsets, list):
        raise TypeError("Input must be a list.")
    
    if len(offsets) == 0:
        return None

    # Validate and convert all elements to float for calculation precision
    try:
        numeric_offsets = [float(x) for x in offsets]
    except (TypeError, ValueError):
        raise TypeError("All elements in the list must be integers or floats.")

    max_offset = max(numeric_offsets)
    min_offset = min(numeric_offsets)
    
    return abs(max_offset - min_offset)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, no network, no files)
    test_cases = [
        ([0, 5, -3], "Test case 1: Mixed positive and negative offsets"),
        ([-2.5, -1.5, 4.0], "Test case 2: Floats with decimals"),
        ([+8, +9, +7], "Test case 3: Positive only"),
        ([-12, -6, -18], "Test case 4: Negative only")
    ]

    for offsets, description in test_cases:
        result = calculate_offset_difference(offsets)
        print(f"{description}: Difference is {result}")