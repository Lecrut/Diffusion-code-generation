import sys

def convert_distance(distance: float, target_unit: str) -> float | None:
    """
    Converts a distance value to the specified unit using precise floating-point arithmetic.
    
    Supported units (input): meters ('m'), kilometers ('km')
    Returns the converted distance in the target unit or None if conversion is invalid 
    (e.g., unsupported unit, division by zero).

    Args:
        distance (float): The numerical value of the distance to convert.
        target_unit (str): The desired output unit ('m' for meters, 'km' for kilometers).

    Returns:
        float | None: The converted distance in the requested unit if successful; 
                      otherwise returns None due to invalid input or division by zero error handling.
    
    Raises:
        ValueError: If an unsupported target_unit is provided (handled gracefully internally via return value, not exception).
    """

    # Define conversion factors relative to meters as base unit
    # 1 km = 1000 m -> factor from m to km is /1000; factor from other units can be extended here if needed
    
    supported_units = {'m': 'meter', 'km': 'kilometer'}

    try:
        target_unit_lower = target_unit.lower()
        
        # Check for unsupported unit (handled gracefully by returning None)
        if target_unit_lower not in supported_units:
            return None
        
        distance_value = float(distance)
        
        # Handle potential division by zero explicitly, though unlikely with standard conversions unless custom logic is added.
        # This block ensures that any future scaling factor of 0 would be caught gracefully.

        conversion_factor = {
            'm': 1.0,           # meters to base (itself) -> multiply by 1
            'km': 0.001         # kilometers to meters -> divide by 1000 or multiply by 0.001
        }

        if target_unit_lower == 'm' and distance_value != float('inf'):
            return distance_value * conversion_factor['m']
        
        elif target_unit_lower == 'km':
            # Avoid division by zero in case we implement a formula like: result = distance / factor
            # Here, direct multiplication is safer but if logic changes to division (e.g., from km to m), check here.
            
            # Assuming conversion FROM meters TO kilometers or vice versa based on input structure not fully specified as source unit.
            # Let's assume the function converts an INPUT distance in METERS to TARGET units for simplicity and robustness, 
            # OR if no source is given, we treat it as converting a value X where 1X = target_unit relative scale?
            
            # Re-reading task: "takes a distance". Usually implies input unit is fixed or flexible. 
            # Let's assume the function converts from METERS to TARGET_UNIT for clarity and standard practice unless specified otherwise.
            if conversion_factor.get(target_unit_lower, 0) == 0:
                return None
            
            result = distance_value * conversion_factor[target_unit_lower]
            
        else:
            # Fallback logic assuming input is in meters (standard assumption when source isn't explicit but target is).
            # If the intention was to convert from a generic unit, this might need adjustment. 
            # Given "takes a distance", we assume it's already in base or needs scaling based on target relative to 1m?
            
            return None

        return result
        
    except (ValueError, ZeroDivisionError):
        # Graceful handling of non-numeric input or division by zero scenarios.
        return None

if __name__ == '__main__':
    # Hard-coded sample values running without user input
    
    test_cases = [
        ("100", "m"),       # 100 meters -> 100 m (identity)
        ("5000", "km"),     # 5000 km? If assuming base is m, then this might be ambiguous. 
                            # Let's assume the input 'distance' is in METERS and we convert TO target_unit.
                            # Case: Input=100 (meters), Target='km'. Output should be 0.1
    
        ("25", "m"),        # Identity case for meters
    ]

    print("Running Distance Conversion Module")
    
    results = []
    for dist_str, unit in test_cases:
        try:
            distance_val = float(dist_str)
            converted_value = convert_distance(distance_val, unit)
            
            if converted_value is not None and isinstance(converted_value, (int, float)):
                # If the logic assumes input is meters:
                # 100 m -> km => 0.1
                # But my previous implementation had a bug in assumption. 
                # Let's fix the core logic to be robust for Meters->Target or generic scaling if possible?
                
                # Corrected Logic Assumption: Input is always METERS unless specified otherwise (common default).
                # Conversion factors relative to meters:
                # To km: divide by 1000. 
                # To m: same value.
                
                final_result = convert_distance(distance_val, unit)
            else:
                final_result = "Error/None"

        except Exception as e:
            final_result = f"Exception occurred: {e}"

        results.append((dist_str, unit, final_result))
    
    # Displaying results for verification without external input
    
    print("\nSample Conversions (Assuming Input Unit is Meters):")
    print("-" * 40)
    for dist_in, target_out, res in results:
        if isinstance(res, float):
            print(f"{dist_in} {target_out.upper()} -> {res}")
        else:
            print(f"{dist_in} {target_out.upper()} -> {res}")