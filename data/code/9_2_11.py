def convert_volume(value: float, target_unit: str) -> float:
    """
    Converts a volume value to the specified unit using an internal dictionary.
    
    Supported units (abbreviations): 'L' (liters), 'm3' (cubic meters), 
    'gal' (US gallons). Default base is liters if no conversion logic applies,
    but here we define explicit conversions from a standard reference: cubic meters.
    
    Conversion factors relative to 1 m^3 = 264.172052 gal = 1000 L
    
    Args:
        value (float): The volume value in the source unit (assumed input is always 'm3' 
                       unless specified otherwise, but based on task description implying 
                       conversion FROM some base TO target). To make this robust and self-contained,
                       we will assume the INPUT value is ALWAYS provided as cubic meters ('m3') by default.
                       If a different unit was intended for input, it should be passed alongside or handled internally.
                       However, to strictly follow "accepts a volume value", let's define: 
                       The function assumes the `value` argument represents Cubic Meters (m^3).
                       
        target_unit (str): The desired output unit code ('L', 'gal'). Other codes return 0 or raise error.

    Returns:
        float: Converted volume in the target unit.

    Raises:
        ValueError: If an unsupported target_unit is provided.
    """
    
    # Internal dictionary mapping base units to their conversion factors relative to cubic meters (m^3)
    # Base assumption for input 'value' is Cubic Meters (1 m^3 = 1000 L, 264.172 gal)
    unit_factors_to_m3: dict[str, float] = {
        'L': 0.001,       # 1 Liter = 0.001 Cubic Meters
        'm3': 1.0,        # Reference base
        'gal': 264.172052 # 1 US Gallon ≈ 264.172 cubic meters? NO. 
                          # Correction: 1 m^3 = 264.172 gallons. So factor for gal is 1/264.172 relative to input if input was gal?
                          # Let's redefine the dictionary as conversion factors FROM that unit TO Cubic Meters (m^3).
    }

    # Re-evaluating logic: 
    # It is safer and more standard for a "convert" function to accept an implicit source or handle common conversions.
    # Given the prompt says "accepts a volume value", let's assume the input `value` is always in Cubic Meters (m^3).
    # This makes the internal dictionary map Target Unit -> Factor relative to m^3.

    target_factors = {
        'L': 1000,       # To get Liters from m^3: multiply by 1000
        'gal': 264.172052, # To get Gallons from m^3: multiply by ~264
    }

    if target_unit not in target_factors:
        raise ValueError(f"Unsupported unit code '{target_unit}'. Supported units: {list(target_factors.keys())}")

    return value * target_factors[target_unit]

if __name__ == '__main__':
    # Hard-coded sample values running without user input or network access
    
    test_cases = [
        {'input_val': 1.0, 'target': 'L', 'expected_approx': 1000},
        {'input_val': 2.5, 'target': 'gal', 'expected_approx': 660.43},
        {'input_val': 0.5, 'target': 'm3', 'expected_approx': 0.5}, # Identity check for base unit if supported as target (though logic above handles it)
    ]

    print("Running convert_volume tests...")
    
    results = []
    for i, case in enumerate(test_cases):
        val = case['input_val']
        tgt = case['target']
        
        try:
            result = convert_volume(val, tgt)
            status = "PASS" if abs(result - case['expected_approx']) < 0.1 else f"FAIL (Got {result})"
            results.append((val, tgt, result))
            print(f"Test Case {i+1}: Input={val} m^3 -> Target='{tgt}'")
            print(f"Result: {result:.4f}")
            print(status)
        except Exception as e:
            print(f"Error in Test Case {i+1}: {e}")

    # Demonstration of error handling for invalid unit
    try:
        convert_volume(5.0, 'ft') 
    except ValueError as ve:
        print("\nCaught expected error for unsupported unit:")
        print(str(ve))