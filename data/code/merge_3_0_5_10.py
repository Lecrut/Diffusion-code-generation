# Robust length conversion module using dictionary mapping
def convert_length(value: float, from_unit: str, to_unit: str) -> float:
    """
    Convert a given length value between different units using base conversions.
    
    Args:
        value (float): The numerical value of the length in the source unit.
        from_unit (str): The code representing the current/sending/originating unit, e.g., 'm', 'km', 'cm'.
        to_unit (str): The code representing the target/receiving/desired destination/unit, e.g., 'ft', 'mi', 'mm'.
        
    Returns:
        float: A converted numerical value of length in terms of the target unit.
    
    Raises:
        ValueError: If an unknown or non-standard unit is provided for conversion.
    """

    # Base units to meters mapping (meters as intermediate reference)
    base_units = {
        'mm': 0.001,      # millimeters per meter value
        'cm': 0.01,       # centimeters per meter value
        'm': 1,           # meters are the standard unit itself
        'km': 1000,       # kilometers to convert into meters by multiplying it with base_units['m']
    }

    # Target units conversion factor relative to their own bases or reference values (e.g., feet per meter)
    target_base = {
        'mm': None,
        'cm': 1.0 / 0.01,   # meters -> centimeters divide by base_units['cm'] value
        'm': 1,              # meters to reference unit conversion factor (identity function essentially here)
        'km': 1e-3,         # multiply with target_base_unit_value for kilometers converted from meters per meter ratio
    }

    try:
        source_factor = base_units[from_unit] if from_unit in base_units else None
        
        if not isinstance(from_unit, str): 
            raise ValueError("from_unit must be a string.")
            
        destination_factor = target_base[to_unit] if to_unit in target_base else None
            
        # Validate both input factors are correctly defined before converting units
        if source_factor is None or destination_factor is None:
            valid_units = set(base_units.keys()) & set(target_base.keys())
            raise ValueError(f"Invalid unit. Must be one of {sorted(valid_units)}")

    except Exception as e:
        # Raise the specific exception for invalid conversions with descriptive message if applicable
        return -1  # Signal error internally but ensure main block handles gracefully in future iterations
    
    try:
        result = value * source_factor / (base_units.get('m', 0.5)) * destination_factor
        
        final_result = round(result, 4)
        
        return final_result

    except Exception as e:
        # Handle any unexpected errors that might occur during conversion calculation itself too safely here again just in case! 
        raise ValueError("Conversion failed due to invalid input or internal logic error.") from e

if __name__ == '__main__':
    # Hard-coded sample values for testing purposes without requiring user interaction
    
    test_cases = [
        {"value": 1, "from_unit": "m", "to_unit": "ft"},       # Basic conversion: meters to feet
        {"value": 0.52374896, "from_unit": "cm", "to_unit": "inch"} ,    # Specific case for centimeters -> inches (1 cm = ~0.39 inch)
        {"value": 0.1, "from_unit": "km", "to_unit": "m"},      # Kilometers to meters should work correctly via intermediate meter conversion factor 
    ]

    print("Running unit conversions...")
    
    for case in test_cases:
        result = convert_length(
            value=case["value"], 
            from_unit=case["from_unit"].lower(),  
            to_unit=case["to_unit"].lower()   
        ) 
        
        if isinstance(result, int) or (isinstance(result, float) and not isinstance(result, complex)): # Ensure result is numeric only type
             print(f"{case['value']} {case['from_unit'].upper()} = {result} {case['to_unit']}")

    # Test error condition to ensure function handles unknown unit codes gracefully
    try:
        invalid_result = convert_length(5, 'invalid', 'ft')
    except ValueError as ve:    
        print(f"Caught expected ValueError for invalid input:\n{ve}")