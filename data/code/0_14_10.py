def convert_length(length, target_unit):
    """
    Converts a numerical length to a predefined set of supported units: 
    meters (m), feet (ft), kilometers (km).
    
    Args:
        length (float or int): The numerical value representing the length.
        target_unit (str): The target unit string for conversion ('m', 'ft', 'km').
        
    Returns:
        float: The converted length as a number corresponding to the target unit.
        
    Raises:
        ValueError: If the provided target_unit is not one of the supported units.
    """
    
    # Define base value in meters and conversion factors for other units relative to meters
    METERS_PER_KM = 1000.0
    METERS_PER_FT = 3.28084
    
    if target_unit == 'm':
        return float(length)
    elif target_unit == 'km':
        # Convert length (assumed in meters based on input context or treat as raw number? 
        # Based on typical usage, the function likely takes a value *in* some unit. 
        # However, without an explicit source unit argument, we must assume the input is already 
        # in base units (meters) to perform conversions TO other units consistently.
        return length / METERS_PER_KM
    elif target_unit == 'ft':
        return length * METERS_PER_FT
    else:
        raise ValueError(f"Unsupported unit '{target_unit}'. Supported units are m, ft, km.")

if __name__ == '__main__':
    # Sample test cases with hard-coded values
    
    # Test 1: Convert 50 meters to feet
    result_m_to_ft = convert_length(50.0, 'ft')
    
    # Test 2: Convert 3 kilometers to meters (assuming input is in km? 
    # Re-evaluating the task prompt: "takes a numerical length". Usually implies magnitude only.
    # To make it functional without source unit context, we assume the input number represents 
    # the quantity of that specific dimension relative to base units or simply convert 
    # from meters (standard SI) to others as per standard conversion logic where 'm' is base).
    # Let's strictly follow: Input = magnitude. Output = same magnitude in target unit? No, that changes value.
    # Standard interpretation for such tasks without source_unit arg: The input number IS the length 
    # expressed in meters (base), and we convert it to others. OR, the user expects us to know context.
    # Given "numerical length", let's assume the input is always treated as Meters unless specified otherwise?
    # Actually, a safer purely functional approach without source unit: Assume input is value IN METERS 
    # and output is in TARGET UNIT. This avoids ambiguity of missing 'source_unit' parameter.
    
    result_km_to_m = convert_length(1000.0, 'm')  # Input as meters -> Output meters (identity)
    result_5km_ft = convert_length(2640.0, 'ft')   # Convert hypothetical meter value to feet
    
    print(f"Converted {result_m_to_ft} ft")
    print(f"Result for km test: {result_km_to_m}")