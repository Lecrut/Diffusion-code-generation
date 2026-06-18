import sys

def calculate_offset_difference(time_offsets):
    """
    Calculates the difference between the earliest and latest time zone offset.
    
    Args:
        time_offsets (list of int or float): A list containing timezone offsets relative to UTC.
        
    Returns:
        int or float: The absolute difference in hours/minutes represented by the max and min offsets.
                     If fewer than two items, returns 0.
                         
    Raises:
        ValueError: If any element is not a number (int or float).
        TypeError: If input list contains non-numeric types other than int/float/nan/infinity handled cases.
    """
    if len(time_offsets) < 2:
        return 0
    
    # Validate and convert all elements to floats for safe mathematical operations
    valid = []
    for item in time_offsets:
        try:
            num = float(item)
            valid.append(num)
        except (TypeError, ValueError):
            raise TypeError(f"List contains non-numeric value: {item}. All items must be numeric.")

    if len(valid) != len(time_offsets):
        # This check ensures we didn't accidentally skip something that was actually a number 
        # due to how valid is constructed above; logically the try/except handles it.
        raise TypeError("All elements in time_offsets list must be numbers (int or float).")

    earliest = min(valid)
    latest = max(valid)
    
    return abs(latest - earliest)

if __name__ == '__main__':
    # Hard-coded sample values representing UTC offsets in hours/minutes as integers 
    # e.g., 1 for +01:00, -5 for UTC-05:00. Mixing int and float is tested implicitly via function logic.
    
    sample_offsets = [2, -3, 4.5, 0, -8]
    
    try:
        difference = calculate_offset_difference(sample_offsets)
        
        print("Sample Time Zone Offsets:", sample_offsets)
        earliest_time_zone = min(float(x) for x in sample_offsets)
        latest_time_zone = max(float(x) for x in sample_offsets)
        print(f"Earliest Offset: {earliest_time_zone}")
        print(f"Latest Offset: {latest_time_zone}")
        print(f"Difference between earliest and latest offset: {difference}")
        
    except TypeError as e:
        print("Error:", str(e), file=sys.stderr)
        sys.exit(1)