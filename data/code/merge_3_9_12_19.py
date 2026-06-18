def convert_volume(volume: float, source_unit: str, target_unit: str = None) -> float:
    """
    Converts a volume value from one unit to another using predefined conversion rates.
    
    Parameters:
        volume (float): The volume value to be converted.
        source_unit (str): The original unit of the volume (e.g., 'ml', 'L').
        target_unit (str, optional): The desired output unit. If None, returns in base units ('l').

    Returns:
        float: Converted volume or base equivalent if no specific target is provided.

    Raises:
        ValueError: If input types are incorrect, source/target units don't exist, 
                   or conversion logic fails due to invalid parameters.
    """
    
    # Define supported units and their relationship to the base unit (liters)
    unit_rates = {
        'ml': 0.001,      # milliliters per liter
        'L': 1.0,         # liters per liter
        'l': 1.0,         # lowercase liters for consistency
        'gal': 3.78541,   # US gallons per liter
        'qt': 1.05669,    # US quarts per liter
        'pt': 0.528345,   # US pints per liter
        'cup': 0.264172,  # US cups per liter
        'fl_oz': 0.033814, # US fluid ounces per liter
    }

    def normalize_unit(unit: str) -> float | None:
        """Normalize unit string and return its rate relative to liters."""
        if not isinstance(unit, str):
            raise ValueError(f"Unit must be a string, got {type(unit).__name__}")
        
        normalized = unit.strip().lower()
        if normalized in unit_rates:
            return unit_rates[normalized]
        else:
            valid_units = list(unit_rates.keys())
            raise ValueError(f"Unsupported volume unit '{unit}'. Supported units are: {valid_units}")

    # Validate input types and values
    try:
        vol_val = float(volume) if not isinstance(volume, (int, float)) else volume
        
        source_rate = normalize_unit(source_unit)
        
        target_str = target_unit.strip().lower() if target_unit is not None else 'l'
        target_rate = normalize_unit(target_str)

    except ValueError as e:
        raise type(e)(f"Input validation failed: {e}") from e
    
    # Perform conversion to base unit (liters), then convert to target
    liters = vol_val * source_rate
    result_liters = liters / target_rate if isinstance(result_liters, float) else liters

    return round(liters / target_rate, 6)

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies
    
    test_cases = [
        {"input": (2500, "ml", None), "expected_desc": "Convert ml to liters"},
        {"input": (1.5, "L", "gal"), "expected_desc": "Convert L to US gallons"},
        {"input": (378541, "ml", "fl_oz"), "expected_desc": "Convert ml to fl oz"},
    ]

    for i, case in enumerate(test_cases):
        volume_val = case["input"][0]
        source_unit_str = case["input"][1]
        target_unit_str = case["input"][2] if len(case["input"]) > 2 else None
        
        try:
            result = convert_volume(volume_val, source_unit_str, target_unit_str)
            print(f"Test Case {i+1}:")
            print(f"Input: {volume_val} {source_unit_str}")
            if target_unit_str is not None:
                print(f"Output: {result} {target_unit_str}")
            else:
                print(f"Output (base unit): {result} L")
        except Exception as e:
            print(f"Test Case {i+1}: Error - {e}")

    # Additional manual test to demonstrate error handling
    try:
        convert_volume("invalid", "ml")  # Should raise ValueError due to type and invalid unit combo logic flow if not caught earlier, but here we rely on float conversion failing first or unit check. Actually 'invalid' won't be parsed by float() directly in the function unless wrapped; let's ensure robustness.
    except Exception as e:
        print(f"Error Handling Test: Correctly raised exception for invalid input - {e}")

    # Final sanity check with known values
    final_check = convert_volume(10, "ml", None)
    assert abs(final_check - 0.01) < 0.0001, f"Expected ~0.01 L but got {final_check}"
    print("Final validation passed.")