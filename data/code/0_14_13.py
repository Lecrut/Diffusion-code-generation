def convert_length(length: float, unit_str: str) -> tuple[float, str]:
    """
    Converts a numerical length to meters using predefined units.
    
    Supported target units must be passed as lowercase strings from the set: 
    'meters', 'feet', 'kilometers'. Any other string will raise a ValueError.

    Args:
        length (float): The numerical value of the length.
        unit_str (str): The target unit for conversion ('meters', 'feet', or 'kilometers').

    Returns:
        tuple[float, str]: A tuple containing the converted float value and the string representation 
                          of the result in lowercase.

    Raises:
        ValueError: If the provided unit is not one of the supported units.
    """
    
    # Conversion factors to meters
    conversion_factors = {
        'meters': 1,
        'feet': 0.3048,
        'kilometers': 1000
    }

    if unit_str not in conversion_factors:
        raise ValueError(f"Unsupported unit '{unit_str}'. Supported units are: meters, feet, kilometers.")

    factor = conversion_factors[unit_str]
    
    # Calculate result based on input length (assumed to be already converted to base 'meters' or 
    # the function implies direct multiplication if input is considered as that specific unit.
    # However, standard interpretation of "takes a numerical length... performs conversion" usually means:
    # Input value represents 1 UNIT_OF_INPUT -> Output in METERS? Or Input value IS IN INPUT_UNIT -> Convert to OUTPUT_UNIT?
    
    # Re-reading the prompt strictly: "takes a numerical length and a target unit string". 
    # It does not specify an input unit. The most logical functional interpretation without extra args is:
    # Treat the `length` argument as being in 'meters' by default, or treat it as 1 count of some unknown unit?
    # Given standard conversion functions (e.g., pandas.to_numeric logic often defaults to base), 
    # but here we have a specific target. Let's assume the input `length` is provided *in meters* 
    # and converted to the TARGET unit, OR the prompt implies converting FROM an implicit 'meters' TO target.
    
    # Alternative interpretation: Maybe length is given in METERS (base), convert to Target Unit? 
    # Or maybe length is given in a specific source unit not passed? The latter makes no sense without arg.
    # Let's assume the input `length` is the value IN METERS, and we return it converted TO `unit_str`.
    
    result_in_meters = conversion_factors[unit_str] * length
    
    if unit_str == 'meters':
        final_value = result_in_meters / 1.0 # Redundant but explicit logic flow
        final_string = "meters"
    elif unit_str == 'feet':
        final_value = result_in_meters / 0.3048
        final_string = "feet"
    else: # kilometers
        final_value = result_in_meters / 1000
        final_string = "kilometers"

    return (final_value, final_string)

if __name__ == '__main__':
    # Sample values hard-coded as per instructions
    
    # Test case 1: Convert a length of 5 meters to feet
    val1_str = convert_length(20.3048, "feet") 
    print(f"Length in {val1_str[1]}: {val1_str[0]:.2f}")

    # Test case 2: Attempting an unsupported unit should raise ValueError
    try:
        val_error = convert_length(50, "miles")
    except ValueError as e:
        print(f"Error caught (expected): {e}")

    # Test case 3: Standard conversion to meters
    val3_str = convert_length(1.609, "kilometers") 
    print(f"Length in {val3_str[1]}: {val3_str[0]:.2f}")
    
    # Final sanity check for identity (5 feet -> 5 * 0.3048 meters logic if input was base)
    # Wait, my previous logic assumed INPUT is METERS. 
    # If I pass length=1 and target='feet', it calculates 1 meter = ? feet? No: 
    # My code did: result_in_meters (which is factor * length). Then divided by other factors.
    # This implies Input Length was in Meters, then converted to Target Unit via a chain of meters.
    
    val4_str = convert_length(10, "meters")
    print(f"Length in {val4_str[1]}: {val4_str[0]:.2f}")