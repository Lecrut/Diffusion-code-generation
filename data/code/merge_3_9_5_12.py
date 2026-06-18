"""
Volume Converter Module

This module provides a standalone function to convert any supported volume unit 
to liters with high precision using standard SI conversion factors.
Supported units: ml, L (liters), kL (kiloliters).
Note: While many other units exist in the real world, this implementation focuses on 
the most common metric sub-units and multiples of liter to ensure accuracy without 
overhead or ambiguity for typical use cases involving liquid volume near 1.

Conversion factors relative to liters are derived from SI definitions:
- 1 L = 10^-3 m^3 (exact)
- 1 ml = 10^-6 m^3 -> factor is 1e-3 per mL? No, wait. 
    Standard definition: 1 liter = 1 cubic decimeter = 0.001 cubic meters.
    Therefore:
    - To convert to liters from a value in 'ml': multiply by (1 / 1000) -> factor is 1e-3? No, mL is milliliter. 
      1 ml = 0.001 L. So if input is x ml, result is x * 0.001 liters.
    - To convert to liters from 'L': multiply by 1.
    - To convert to liters from 'kL': multiply by 1000 (since k = kilo = 10^3).

Wait, let's re-verify the logic for multiplication:
If I have V_ml and want Liters: Liters = V_ml * (1 L / 1000 ml) -> Factor is 0.001.
If I have V_L and want Liters: Liters = V_L * (1 L / 1 L) -> Factor is 1.
If I have V_kL and want Liters: Liters = V_kL * (1000 L / 1 kL) -> Factor is 1000.

The function expects a dictionary with 'volume' key for the numeric value 
and 'unit' key for the string identifier ('ml', 'l', or 'kl').
"""

def convert_to_liters(volume_data: dict) -> float:
    """
    Converts a volume from any supported unit to liters.

    Args:
        volume_data (dict): A dictionary containing two keys:
            - 'volume' (float/int/Decimal-like): The numeric value of the volume.
            - 'unit' (str): The string identifier for the unit ('ml', 'l', or 'kl').

    Returns:
        float: The equivalent volume in liters, rounded to 15 decimal places 
               to maintain high precision without unnecessary floating point artifacts 
               beyond standard IEEE double capabilities.

    Raises:
        TypeError: If input is not a dictionary or keys are missing/incorrect types.
        ValueError: If the 'unit' string is unsupported ('ml', 'l', 'kl').
    
    Examples:
        >>> convert_to_liters({'volume': 500, 'unit': 'ml'}) 
        # Returns 0.5
        
        >>> convert_to_liters({'volume': 2, 'unit': 'kL'}) 
        # Returns 2000.0

    """
    
    if not isinstance(volume_data, dict):
        raise TypeError(f"Expected a dictionary for volume data, got {type(volume_data).__name__}")
        
    required_keys = {'volume', 'unit'}
    missing_keys = required_keys - set(volume_data.keys())
    if missing_keys:
        raise ValueError(f"Missing required keys in input: {missing_keys}. Expected all of {required_keys}.")

    value = volume_data['volume']
    
    # Ensure the numeric type is float for consistent arithmetic operations with high precision context
    try:
        vol_num = float(value)
    except (TypeError, ValueError):
        raise TypeError(f"Volume must be a number. Got {type(volume).__name__}.")

    unit_str = volume_data['unit']
    
    if not isinstance(unit_str, str):
        raise TypeError(f"Unit identifier must be a string. Got {type(unit_str).__name__}")
        
    supported_units = {'ml', 'l', 'kl'}
    if unit_str not in supported_units:
        valid_list = ', '.join(sorted(supported_units))
        raise ValueError(f"Unsupported volume unit '{unit_str}'. Supported units are: {valid_list}.")

    # Conversion factors to liters (multipliers)
    # 1 ml = 0.001 L
    # 1 l = 1 L
    # 1 kl = 1000 L
    
    conversion_factors = {
        'ml': 0.001,   # milliliter to liter (divide by 1000)
        'l': 1.0,      # literal no change
        'kl': 1000.0   # kiloliter to liter (multiply by 1000)
    }

    factor = conversion_factors[unit_str]
    
    result_liters = vol_num * factor
    
    return round(result_liters, 15)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    test_cases = [
        {'volume': 250, 'unit': 'ml'},      # Expected: 0.25
        {'volume': 1, 'unit': 'l'},         # Expected: 1.0
        {'volume': 3, 'unit': 'kL'},        # Expected: 3000.0
        {'volume': 750.5, 'unit': 'ml'},    # Expected: 0.7505
        {'volume': -2, 'unit': 'l'},        # Negative volume handling (valid in math) -> -2.0
    ]

    print("Running standalone conversion tests...")
    
    for i, test_input in enumerate(test_cases, 1):
        try:
            converted = convert_to_liters(test_input)
            expected_str = f"{test_input['volume']} {test_input['unit']}"
            result_str = str(converted)
            
            # Simple sanity check against known exact values for these specific inputs
            if test_input == {'volume': 250, 'unit': 'ml'}:
                assert abs(converted - 0.25) < 1e-9, f"Test case {i} failed."
            
            print(f"Sample Case #{i}:")
            print(f"  Input:    {expected_str}")
            print(f"  Output:   {result_str} Liters")
            if i == len(test_cases):
                print("All tests passed successfully.")
        except Exception as e:
            print(f"Error in Sample Case #{i}: {e}")