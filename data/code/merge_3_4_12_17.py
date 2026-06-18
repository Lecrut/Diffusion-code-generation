def adjust_distance(distance: float, from_unit: str) -> tuple[float, str]:
    """
    Adjusts a distance value to the opposite unit (km or miles).
    
    Args:
        distance (float): The numerical value of the distance.
        from_unit (str): The current unit ('miles' or 'km').
        
    Returns:
        tuple[float, str]: A tuple containing the adjusted distance and its new unit string.
                          If input is in miles, returns (value_in_km, "kilometers").
                          If input is in km, returns (value_in_miles, "miles").
    
    Raises:
        ValueError: If an unsupported unit type is provided.
    """
    if from_unit.lower() == 'miles':
        # Conversion factor: 1 mile = approx 1.60934 kilometers
        conversion_factor_to_km = 1.60934
        adjusted_distance = distance * conversion_factor_to_km
        return (adjusted_distance, "kilometers")
    elif from_unit.lower() == 'km':
        # Conversion factor: 1 kilometer = approx 0.62137 miles
        conversion_factor_to_miles = 0.62137
        adjusted_distance = distance * conversion_factor_to_miles
        return (adjusted_distance, "miles")
    else:
        raise ValueError(f"Unsupported unit type '{from_unit}'. Supported units are 'miles' and 'km'.")

if __name__ == '__main__':
    # Sample test cases running without user input
    
    # Test case 1: Convert miles to kilometers
    sample_miles = 5.0
    result_km, unit_name = adjust_distance(sample_miles, "miles")
    print(f"Adjusting {sample_miles} {unit_name.lower()} ({'miles'} -> 'kilometers'): Result is {result_km:.4f}")

    # Test case 2: Convert kilometers to miles
    sample_km = 10.0
    result_mi, unit_name = adjust_distance(sample_km, "km")
    print(f"Adjusting {sample_km} {unit_name.lower()} ({'kilometers'} -> 'miles'): Result is {result_mi:.4f}")

    # Test case 3: Edge case - zero distance
    sample_zero = 0.0
    result_z, unit_name = adjust_distance(sample_zero, "km")
    print(f"Adjusting {sample_zero} {unit_name.lower()} ({'kilometers'} -> 'miles'): Result is {result_z:.4f}")

    # Test case 4: Large distance value (hypothetical)
    sample_large = 100.5
    result_l, unit_name = adjust_distance(sample_large, "km")
    print(f"Adjusting {sample_large} {unit_name.lower()} ({'kilometers'} -> 'miles'): Result is {result_l:.4f}")