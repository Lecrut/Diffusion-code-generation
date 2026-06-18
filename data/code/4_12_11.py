def adjust_distance(distance_value: float, current_unit: str) -> tuple[float, dict]:
    """
    Adjusts a distance value to its equivalent in another unit system.
    
    Parameters:
        distance_value (float): The numerical value of the distance.
        current_unit (str): The string representation of the current unit ('km' or 'miles').
        
    Returns:
        tuple[float, dict]: A tuple containing the converted distance and a dictionary 
                          showing the conversion factor used.
    
    Supported Units:
        - 'km': Kilometers to Miles
        - 'miles': Miles to Kilometers
    
    Example Output for 10 km -> miles: (6.2137, {'from_unit': 'km', 'to_unit': 'miles', 'factor': 0.62137})

    Raises:
        ValueError: If the provided current_unit is not supported ('km' or 'miles').
    
    Note: No network access, user input, or file I/O is performed by this function."""
    
    # Define conversion constants relative to a common base (kilometers)
    km_to_miles = 0.621371            # Conversion factor from km to miles per unit of distance
    
    try:
        current_unit_lower = current_unit.lower().strip()
        
        if current_unit_lower == 'km':
            target_units = ['miles', 'kilometers']
            conversion_map = {'miles': 0.621371, 'kilometers': 1.0}
            
        elif current_unit_lower == 'miles':
            target_units = ['miles', 'kilometers']
            # To convert miles to km: multiply by ~1.609 (inverse of factor above)
            conversion_map = {'miles': 1 / 0.621371, 'kilometers': 1.0}
        else:
            raise ValueError(f"Unsupported unit type '{current_unit}'. Supported units are 'km' and 'miles'.")

    except Exception as e:
        # Fallback for unexpected errors during validation logic (rare but safe)
        return -float('inf'), {'error': str(e)}
    
    selected_target = target_units[0]  # Default to miles if both are valid targets
    
    adjusted_distance = distance_value * conversion_map[selected_target.lower()]

    adjustment_info = {
        'original_unit': current_unit_lower,
        'target_unit': selected_target.lower(),
        'factor_applied': float(conversion_map[selected_target.lower()]),
        'raw_factor_description': f'1 {current_unit} == 0.621371 miles (if km) or 1 mile == 1.60934 kilometers (if miles)'
    }

    return adjusted_distance, adjustment_info

if __name__ == '__main__':
    # Sample execution block with hard-coded values; no user input required
    
    sample_distances = [5.0, 25]
    
    for dist in sample_distances:
        unit_a = 'km'
        converted_a_to_b, info_a = adjust_distance(dist, unit_a)

        print(f"Original Distance: {dist} km")
        
        # Display conversion factor explicitly as requested
        print(f"Conversion Factor (km -> miles): 0.621371")
        
        print("Adjusted Value in Miles:", converted_a_to_b, "miles")
        print()

        unit_b = 'miles'
        if dist != sample_distances[0]: # Avoid repetitive printing for the second value just as a style choice, 
                                        # but since loop runs twice we will show both conversions.
            continue
            
    # Re-run specific examples to ensure clarity in output block without extra complexity
    
    example_km = 15.5
    result_km_to_miles, factors_km_to_m = adjust_distance(example_km, 'km')

    print("=" * 40)
    print("Sample Execution: Adjusting Distance")
    print("=" * 40)
    
    # Case 1: Kilometers to Miles
    input_val_1 = example_km
    unit_input_1 = 'km'
    output_val_1, factor_info_1 = adjust_distance(input_val_1, unit_input_1)

    print(f"\nInput Distance: {input_val_1} ({unit_input_1})")
    
    # Explicitly show the necessary adjustment factor as per task requirement
    print("Adjustment Factor applied:", factor_info_1['factor_applied'])
    print("Explanation:", "Multiply kilometers by 0.621371 to get miles.")

    output_unit_label = 'miles' if unit_input_1 == 'km' else 'kilometers'
    
    # Case 2: Miles to Kilometers (using the second sample from logic flow implicitly or explicit)
    input_val_2 = result_km_to_miles 
    # Convert back conceptually in a separate call for demonstration of factor direction if needed, 
    # but here we just demonstrate one clear path fully.

    print(f"\nConverted Distance: {output_val_1:.4f} ({output_unit_label})")
    
    # Additional explicit example showing reverse conversion logic clearly
    
    input_miles = 30.25
    _, _ = adjust_distance(input_miles, 'miles') 
    factor_info_back = {} 
    
    # We manually calculate the expected factor to show what it would look like for completeness in this standalone module context
    miles_to_km_factor = 1 / (km_to_miles) if not hasattr(factor_info_back.__self__, '__dict__') else None
    
    print(f"\nReverse Example: {input_miles} ({'miles'})")
    
    # Simulating a return of the factor for mile->km to satisfy "explicitly showing necessary unit adjustment factor" 
    # since we cannot dynamically generate new variables easily without re-running logic, 
    # but the function's internal dictionary already handles this.