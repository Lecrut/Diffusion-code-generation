def adjust_distance(distance_value: float, from_unit: str) -> tuple[float, str]:
    """
    Adjusts a distance value to its equivalent in another unit (miles or km).
    
    Parameters:
        distance_value (float): The numerical value of the distance.
        from_unit (str): The current unit ('km' for kilometers or 'mi' for miles).
        
    Returns:
        tuple[float, str]: A tuple containing the adjusted distance and the target unit string.
    
    Unit Conversion Factors:
        1 kilometer = 0.621371 miles
        1 mile = 1.60934 kilometers
    
    Note: This function assumes conversion to the opposite of 'from_unit'.
          If from_unit is 'km', it converts to miles and vice versa.
    """
    
    # Define base unit as meters for internal calculation precision, then convert back if needed? 
    # However, direct factor multiplication is more efficient and explicit per task requirements.
    
    conversion_factor = 0.621371
    
    target_unit_str = ""

    if from_unit.lower() == "km":
        # Convert kilometers to miles: multiply by ~0.621371
        adjusted_value = distance_value * conversion_factor
        return (adjusted_value, "miles")
    
    elif from_unit.lower() == "mi":
        # Convert miles to kilometers: multiply by ~1.60934
        converted_to_km = 1 / conversion_factor
        adjusted_value = distance_value * converted_to_km
        return (adjusted_value, "km")
        
    else:
        raise ValueError("Unsupported unit type. Use 'km' or 'mi'.")

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        {"value": 10, "unit": "km"},      # Convert 10 km to miles
        {"value": 5.2, "unit": "mi"},     # Convert 5.2 mi to km
        {"value": 34, "unit": "miles"},   # Explicit 'miles' input (case-insensitive logic handled inside)
    ]

    for case in test_cases:
        dist_val = case["value"]
        current_unit = case["unit"].lower() if isinstance(case["unit"], str) else case["unit"]
        
        result_dist, target_unit = adjust_distance(dist_val, current_unit)
        
        print(f"Adjusting {dist_val} {current_unit}:")
        print(f"Result: {result_dist:.4f} {target_unit}")