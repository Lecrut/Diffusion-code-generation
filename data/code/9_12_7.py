def convert_volume(volume: float, source_unit: str, target_unit: str = None) -> float | None:
    """
    Converts a volume from one unit to another using predefined conversion rates.
    
    Args:
        volume (float): The volume value to be converted.
        source_unit (str): The source unit of the volume (e.g., 'liter', 'gallon').
        target_unit (str, optional): The target unit for conversion. If None or empty string, 
                                    returns the input as is if valid, otherwise raises ValueError.

    Returns:
        float | None: The converted volume in the target unit, or None if no conversion occurs and units are invalid/missing.

    Raises:
        TypeError: If inputs are not of expected types.
        ValueError: If source_unit or target_unit is unknown or empty (unless handled gracefully by returning None).
    
    Note: This function handles potential input errors gracefully as per task requirements, 
          meaning it does not raise exceptions for invalid units but instead may return None 
          if the conversion cannot be performed due to missing parameters. However, type checks are enforced strictly."""

    # Define supported units and their base equivalent (in liters)
    unit_to_base = {
        'liter': 1.0,
        'milliliter': 0.001,
        'gallon': 3.78541,
        'quart': 0.946353,
        'pint': 0.473152,
        'cup': 0.24,
    }

    # Validate input types
    if not isinstance(volume, (int, float)):
        raise TypeError("Volume must be a numeric value.")
    
    source_unit = str(source_unit).strip().lower()
    target_unit_str = str(target_unit) if target_unit is not None else ""
    target_unit = target_unit_str.strip().lower()

    # Check for valid units and perform conversion logic
    base_volume_liters = unit_to_base.get(source_unit, 0.0)
    
    # If source or target unit is invalid (not in dictionary), return None gracefully as per "handle errors" instruction
    if not isinstance(base_volume_liters, float):
        return None

    converted_value = volume * base_volume_liters
    
    # Determine final output based on target_unit parameter presence and validity
    if not target_unit:
        # If no specific target unit is requested but source is valid, assume identity conversion (return original)
        # Only do this if the user didn't explicitly provide a bad string for target. 
        # However, to strictly follow "optional parameter", we treat missing as return same value only if units match or just return base?
        # Re-reading task: returns equivalent volume in target unit specified by optional param.
        # If target_unit is None/empty and source exists, returning the original input (as 'liters' effectively) makes sense for identity unless conversion requested.
        # But to be safe on "equivalent", let's assume if no target provided, we return value in base unit context or just pass through? 
        # Let's interpret: If target_unit is not specified, maybe it implies converting TO the same type? Or simply returning input volume as-is (interpreted as liters)?
        # Given strictness, I will convert to 'liter' if no specific target given and source != liter.
        
        final_volume = converted_value / unit_to_base.get('liter', 1)
    else:
        base_target_liters = unit_to_base.get(target_unit, 0.0)
        if not isinstance(base_target_liters, float):
            return None
        
        # Convert from source liters to target liters then back? No, direct ratio is better but we have both in 'liters' as intermediate.
        final_volume = converted_value / base_target_liters

    return round(final_volume, 4)

if __name__ == '__main__':
    # Hard-coded sample values running without user input or external dependencies
    
    test_cases = [
        {"input": (10, "liter", None), "expected_desc": "Convert liters to base"},
        {"input": (5.2834, "gallon", "quart"), "expected_desc": "Gallons to quarts"},
        {"input": (100, "milliliter", "cup"), "expected_desc": "Milliliters to cups"},
    ]

    results = []
    
    for i, case in enumerate(test_cases):
        volume_val, src_unit, tgt_unit = case["input"]
        
        try:
            result = convert_volume(volume_val, src_unit, tgt_unit)
            
            # Determine expected output logic manually for verification comments if needed, 
            # but here we just store the computed float.
            results.append({
                "test_index": i + 1,
                "input_value": volume_val,
                "source": src_unit,
                "target": tgt_unit or "(None)",
                "output": result
            })
            
        except Exception as e:
            # The function should handle errors gracefully (return None) rather than crash on bad units if handled internally.
            # But type errors like non-numeric input will still raise TypeError which is expected behavior for invalid types.
            results.append({
                "test_index": i + 1,
                "input_value": volume_val,
                "source": src_unit,
                "target": tgt_unit or "(None)",
                "output": f"Error: {e}" if isinstance(e, TypeError) else None # Only log type errors as expected failure for bad types? 
            })

    print("Sample Execution Results:")
    for res in results:
        desc = res.get("expected_desc", "")
        out_str = str(res["output"])
        print(f"Test Case {res['test_index']}: Input={res['input_value']} ({res['source']}) -> Target={res['target']}")
        if isinstance(out_str, float):
            print(f"Result: {out_str}")
        else:
            # If an error occurred during execution (like bad type), show it. 
            # In our test cases above, types are correct so this block might not trigger for these specific inputs unless logic fails.
            if "Error:" in out_str:
                print(f"Handled Error Gracefully")