def adjust_distance(distance_value: float, current_unit: str) -> tuple[float, str]:
    """
    Adjusts a distance value to its equivalent in another unit system (metric or imperial).
    
    Parameters:
        distance_value (float): The numerical value of the distance.
        current_unit (str): The string representing the current unit ('miles' or 'km').
        
    Returns:
        tuple[float, str]: A tuple containing the adjusted distance and its new unit type.
                          If input is in miles, returns equivalent in km; if in km, returns in miles.
    
    Unit Conversion Factors (explicitly shown):
        1 mile = 1609.34 meters -> to convert miles to kilometers: multiply by 1.60934
        1 kilometer = 1 meter * 1/1000 -> to convert km to miles: divide by 1.60934 (or multiply by ~0.62137)
    """
    
    # Define conversion constants explicitly for clarity and maintainability
    MILES_TO_KM_FACTOR = 1.60934
    KM_TO_MILES_FACTOR = 1 / MILES_TO_KIM_FACTOR
    
    if current_unit.lower() == 'miles':
        adjusted_distance = distance_value * MILES_TO_KM_FACTOR
        new_unit = "km"
    elif current_unit.lower() == 'km':
        adjusted_distance = distance_value * KM_TO_MILES_FACTOR
        new_unit = "miles"
    else:
        raise ValueError(f"Unsupported unit type '{current_unit}'. Supported units are 'miles' and 'km'.")

    return (adjusted_distance, new_unit)

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    # Sample 1: Convert 5 miles to kilometers
    dist_miles = 5.0
    unit_input_1 = "miles"
    
    result_distance, new_unit_1 = adjust_distance(dist_miles, unit_input_1)
    print(f"{dist_miles} {unit_input_1} is equivalent to {result_distance:.4f} {new_unit_1}")

    # Sample 2: Convert 10 kilometers to miles
    dist_km = 10.5
    unit_input_2 = "km"
    
    result_distance, new_unit_2 = adjust_distance(dist_km, unit_input_2)
    print(f"{dist_km} {unit_input_2} is equivalent to {result_distance:.4f} {new_unit_2}")

    # Sample 3: Edge case - zero distance
    dist_zero = 0.0
    
    result_distance, new_unit_3 = adjust_distance(dist_zero, "miles")
    print(f"{dist_zero} {unit_input_1} is equivalent to {result_distance:.4f} {new_unit_3}")

    # Sample 4: Large distance value for precision check
    dist_large = 250.7
    
    result_distance, new_unit_4 = adjust_distance(dist_large, "km")
    print(f"{dist_large} {unit_input_2} is equivalent to {result_distance:.4f} {new_unit_4}")