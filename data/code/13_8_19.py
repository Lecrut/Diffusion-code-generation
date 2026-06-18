def calculate_offset_difference(offsets):
    """
    Calculates the difference between the earliest and latest time zone offset.
    
    Parameters:
        offsets (list of int or float): A list containing numeric timezone offsets relative to UTC.
        
    Returns:
        float: The absolute difference in hours/units between the maximum and minimum offset values.
              Raises ValueError if input is not a non-empty list of numbers.
              
    Example:
        >>> calculate_offset_difference([0, 5, -3])
        8.0
    """
    if not isinstance(offsets, list) or len(offsets) == 0:
        raise ValueError("Input must be a non-empty list.")
    
    # Ensure all elements are numeric and convert to float for consistent calculation
    try:
        converted_offsets = [float(x) for x in offsets]
    except (TypeError, ValueError):
        raise TypeError(f"All elements in the offset list must be numbers. Got {type(offsets[0])} instead.")

    max_offset = max(converted_offsets)
    min_offset = min(converted_offsets)
    
    return abs(max_offset - min_offset)

if __name__ == '__main__':
    # Hard-coded sample values as per requirements (no user input, files, or network access)
    sample_data_1 = [0.0, 5.25, -3.5]      # Mixed positive/negative offsets including decimals
    sample_data_2 = [-8, -4, 6, 9]         # Integer offsets representing US/Europe time zones roughly
    
    result_1 = calculate_offset_difference(sample_data_1)
    result_2 = calculate_offset_difference(sample_data_2)
    
    print(f"Sample Data 1 Offsets: {sample_data_1}")
    print(f"Difference (Earliest to Latest): {result_1} hours")
    
    print("\nSample Data 2 Offsets:", sample_data_2)
    print("Difference (Earliest to Latest):", result_2, "hours")