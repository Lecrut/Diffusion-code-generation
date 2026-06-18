def adjust_distance(distance: float, unit_type: str) -> tuple[float, str]:
    """
    Adjusts a distance value to its equivalent in another unit system.
    
    Args:
        distance (float): The numerical value of the distance.
        unit_type (str): The current unit ('miles' or 'km'). Returns the converted 
                         value and the target unit string.

    Returns:
        tuple[float, str]: A tuple containing the adjusted distance as a float 
                          and the new unit type as a string.

    Note:
        Conversion factors used relative to kilometers (1 km = 0.621371 miles).
        - If input is 'miles', output is in 'km'. Factor applied: divide by 0.621371.
        - If input is 'km', output is in 'miles'. Factor applied: multiply by 0.621371.
    """
    
    # Define conversion factors relative to the base unit (kilometers)
    miles_to_km_factor = 1 / 0.621371
    km_to_miles_factor = 0.621371

    if unit_type == 'miles':
        adjusted_distance = distance * miles_to_km_factor
        target_unit = "km"
    elif unit_type == 'km':
        adjusted_distance = distance * km_to_miles_factor
        target_unit = "miles"
    else:
        raise ValueError(f"Unsupported unit type '{unit_type}'. Supported units are 'miles' and 'km'.")

    return adjusted_distance, target_unit

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    # Test case 1: Convert 5 miles to km explicitly showing the factor logic
    result_miles_to_km = adjust_distance(5.0, 'miles')
    
    print("Sample Execution Results:")
    print("-" * 30)
    
    distance_input_1, unit_output_1 = result_miles_to_km
    # The function internally applies the factor: 5 miles / 0.621371 ≈ 8.046 km
    
    print(f"Input Distance: {distance_input_1} {unit_output_1}")
    
    # Test case 2: Convert 10 kilometers to miles explicitly showing the factor logic
    result_km_to_miles = adjust_distance(10.0, 'km')
    
    distance_input_2, unit_output_2 = result_km_to_miles
    
    print(f"Input Distance: {distance_input_2} {unit_output_2}")