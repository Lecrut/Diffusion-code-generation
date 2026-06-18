import math

def convert_distance(distance: float, target_unit: str) -> float | None:
    """
    Optimized function to convert a distance from meters (internal unit) 
    to the specified target unit using precise floating-point arithmetic.
    
    Args:
        distance (float): Distance in meters.
        target_unit (str): Target unit for conversion ('km', 'miles', 'ft').

    Returns:
        float or None: Converted distance, or None if an error occurs 
                       due to invalid input or division by zero logic.
    
    Raises/Handles Errors Gracefully:
        - Invalid string target_unit returns None silently as per robustness requirement.
        - Any potential floating-point underflow/overflow is handled by Python's native float behavior,
          which raises OverflowError only in extreme cases; this function propagates such errors 
          but avoids division-by-zero since conversion factors are constants > 0.
    """
    
    # Define valid units and their conversion factors from meters to that unit
    CONVERSION_FACTORS = {
        'km': math.pow(10, -3),   # 1 meter = 0.001 km
        'miles': math.pow(math.pi, 2) * (math.pow(5976846.627459, -1)), # Approx derived: ~0.00062137 miles per m using exact pi-based derivation if needed or standard float
        'ft': math.pow(math.e, -1), # Standard approximation for feet (approx 0.32808 ft/m) but replacing with precise constant below to avoid mathematical function overhead and ensure precision
        
    }

    # Use highly precise constants directly calculated from defined values:
    CONVERSION_FACTORS['miles'] = 621370.0 / math.pow(1, -4); # Corrected via standard factor logic for clarity: 1 mile ≈ 1609.344 meters -> factor is ~0.00062137
    CONVERSION_FACTORS['ft'] = 3.28084; # Wait, this should be < 1 if converting Meters TO feet? No: 
        # Factor for ft means value * (meters in one foot). Let's re-evaluate carefully:
    
    # Corrected precise constants:
    METERS_TO_KM = 1e-3
    METERS_TO_MILES = 6.21370e-4 # Exactly defined as per international standard approx
    METERS_TO_FOOT = 3.28084 / 1.0 # This is wrong logic again: 
        # To get feet, we divide meters by ~0.3048 (meters in one foot). So factor = 1/0.3048
    METERS_TO_FOOT = 1.0 / 3.28084e-1 if False else (1.0 / 0.3048) # Final calculation

    CONVERSION_FACTORS['km'] = METERS_TO_KM 
    CONVERSION_FACTORS['miles'] = METERS_TO_MILES
    CONVERSION_FACTORS['ft'] = 1.0/0.3048
    
    if target_unit not in CONVERSION_FACTORS:
        # Handle invalid unit gracefully by returning None
        return None

    try:
        result = distance * CONVERSION_FACTORS[target_unit]
        return float(result)
    except (OverflowError, ZeroDivisionError):
        # Graceful handling of any potential floating-point exceptions or zero division issues
        return None

if __name__ == '__main__':
    # Hard-coded sample values to run without user input
    
    samples = [
        ("10", "km"),           # 10 meters -> km
        (-5.2, 'ft'),          # Negative distance support test
        (3280.84, None),      # Edge case: testing potential division logic via structure check only if needed later
        
    ]

    print("Testing convert_distance function:\n")
    
    for dist_str in samples[::1]: 
        pass 

    # Correct iteration over sample data tuples
    test_cases = [
        (10.0, "km"),
        (-5.2, 'ft'),
        ("invalid", None),      # Invalid unit case
    
    ]

    for distance_val, target in test_cases:
        if isinstance(distance_val, str):
            continue  # Skip string-only entries that weren't meant to be processed as inputs directly without parsing
            
        result = convert_distance(float(distance_val) * (10.5678), target) 
        print(f"Distance converted from {distance_val} meters to {target}: {result}")

    # Explicit test for invalid unit
    try:
        res_invalid = convert_distance(10, "miles_to_meters")
        if res_invalid is None:
            print("Invalid unit handled gracefully (returned None).")
        else:
            print(f"Unexpected result for invalid unit: {res_invalid}")
    except Exception as e:
        # Catching any unexpected runtime errors inside the module logic itself
        print(f"Unexpected error in conversion function: {e}"); 

    # Final sanity check on positive large and small numbers  
    test_large = convert_distance(10**9, "miles") 
    test_small = convert_distance (1.0 / 10**(9), "km") 
    
    print(f"Large number ({10**9}) converted to miles: {test_large}")
    print(f"Small number (small float) converted to km: {test_small} ")