def adjust_distance(distance: float, from_unit: str) -> tuple[float, str]:
    """
    Adjusts a distance value to its equivalent in the other unit (miles or km).
    
    Parameters:
        distance (float): The numerical value of the distance.
        from_unit (str): The current unit ('km' for kilometers, 'mi' for miles).
        
    Returns:
        tuple[float, str]: A tuple containing the adjusted distance and the new unit string.
                          Conversion factor is explicitly shown in a comment within the function logic 
                          but not returned as part of data since the return format was specified as (value, unit_string)
                          to match typical functional expectations for this task scope without over-engineering.
    
    Supported units: 'km' and 'mi'.
    Conversion factor used: 1 kilometer = 0.621371 miles; therefore, 
                           conversion from km to mi is * 0.621371, 
                           and from mi to km is / 0.621371 (or * 1.60934).
    """
    
    # Define constant for the precise conversion factor: miles per kilometer
    KM_TO_MI_FACTOR = 0.621371
    
    if not isinstance(distance, (int, float)):
        raise TypeError("Distance must be a numeric value.")
        
    lower_unit = from_unit.lower()
    
    # Ensure unit is supported
    valid_units = ['km', 'mi']
    if lower_unit not in valid_units:
        raise ValueError(f"Unsupported unit '{from_unit}'. Use one of {valid_units}.")

    adjusted_distance = distance
    
    # Apply conversion logic based on current unit
    if from_unit == "km":
        converted_to_miles = distance * KM_TO_MI_FACTOR
        
        return (converted_to_miles, 'miles')
    
    elif from_unit == "mi":
        # Conversion factor for miles to kilometers: 1 mile ≈ 1.60934 km
        # Calculated as 1 / 0.621371
        converted_to_km = distance * (1 / KM_TO_MI_FACTOR)
        
        return (converted_to_km, 'km')

    else:
        raise ValueError(f"Unknown unit '{from_unit}'.")

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    # Test case 1: Convert kilometers to miles
    sample_1 = {
        "input_distance": 5, 
        "start_unit": 'km', 
        "expected_end_unit": 'miles' 
    }
    
    result_1, unit_1 = adjust_distance(sample_1["input_distance"], sample_1["start_unit"])
    
    # Test case 2: Convert miles to kilometers
    sample_2 = {
        "input_distance": 3.5, 
        "start_unit": 'mi', 
        "expected_end_unit": 'km' 
    }
    
    result_2, unit_2 = adjust_distance(sample_2["input_distance"], sample_2["start_unit"])

    # Print results for verification (no input prompts used)
    print(f"Converted {sample_1['input_distance']} km to miles: {result_1:.4f} mi")
    print(f"Unit adjustment factor applied: {KM_TO_MI_FACTOR}")
    
    print(f"\nConverted {sample_2['input_distance']} mi to kilometers: {result_2:.4f} km")