def adjust_distance(distance_value: float, from_unit: str) -> tuple[float, dict]:
    """
    Adjusts a distance value to an alternative unit system (metric/imperial).
    
    Args:
        distance_value: The numerical value of the distance.
        from_unit: String indicating 'miles' or 'km'.

    Returns:
        A tuple containing:
            - Converted float value in kilometers if input was miles, or vice versa.
            - A dictionary showing the conversion factor used and source unit name.
    
    Supported units are explicitly handled via a fixed set of constants to avoid external dependencies.
    """
    
    # Define explicit conversion factors relative to meters as base reference for clarity
    METERS_PER_KM = 1000.0
    KM_TO_MILES_FACTOR = 0.621371192
    MILES_TO_KM_FACTOR = 1.609344
    
    if from_unit.lower() not in ['miles', 'km']:
        raise ValueError(f"Unsupported unit type '{from_unit}'. Supported: 'miles' or 'km'.")
    
    conversion_details = {}
    
    # Determine target unit and apply factor explicitly showing the adjustment logic
    is_miles_input = from_unit.lower() == 'miles'
    
    if is_miles_input:
        # Convert miles to kilometers
        # Logic: Miles * (1.609344) = Kilometers
        adjusted_distance_km = distance_value * MILES_TO_KM_FACTOR
        conversion_details['factor'] = str(MILES_TO_KM_FACTOR)
        conversion_details['description'] = f"Miles multiplied by {MILES_TO_KM_FACTOR}"
    else:
        # Convert kilometers to miles
        # Logic: Kilometers / (1.609344) or Kilometers * 0.621371... = Miles
        adjusted_distance_miles = distance_value * KM_TO_MILES_FACTOR
        conversion_details['factor'] = str(KM_TO_MILES_FACTOR)
        conversion_details['description'] = f"Kilometers multiplied by {KM_TO_MILES_FACTOR}"
    
    return (adjusted_distance_km if is_miles_input else adjusted_distance_miles, 
            conversion_details)

if __name__ == '__main__':
    # Sample execution block with hard-coded values
    # No user input or external dependencies required
    
    sample1_value = 5.0
    sample1_unit = 'miles'
    
    result1_dist, details1 = adjust_distance(sample1_value, sample1_unit)
    
    print(f"Input: {sample1_value} {sample1_unit}")
    print(f"Conversion Details: Factor={details1['factor']}, Description={details1['description']}")
    print(f"Adjusted Distance (km): {result1_dist:.6f}\n")
    
    sample2_value = 35.0
    sample2_unit = 'km'
    
    result2_dist, details2 = adjust_distance(sample2_value, sample2_unit)
    
    print(f"Input: {sample2_value} {sample2_unit}")
    print(f"Conversion Details: Factor={details2['factor']}, Description={details2['description']}")
    print(f"Adjusted Distance (miles): {result2_dist:.6f}\n")