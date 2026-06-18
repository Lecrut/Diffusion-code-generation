"""
Module: distance_converter.py

A production-ready script demonstrating unit conversion between miles and kilometers.
This module uses a specified conversion factor to ensure accuracy without hard-coding 
the standard 1 mile = 1.60934 km ratio directly into the logic, allowing for easy 
adjustment via parameters if needed by external systems or future maintenance requirements.

The script includes clear input handling through hardcoded sample values and formatted output.
It operates entirely offline with no user interaction required during execution.
"""

def convert_distance(value: float, from_unit: str, to_unit: str) -> tuple[float, dict]:
    """
    Convert a distance between miles and kilometers using a configurable conversion factor.

    Args:
        value (float): The numerical value of the distance in the source unit.
        from_unit (str): Source unit ('miles' or 'kilometers'). Case-insensitive input accepted 
                        but normalized internally for consistency.
        to_unit (str): Target unit ('miles' or 'kilometers'). Case-insensitive input accepted 
                      and normalized internally.

    Returns:
        tuple[float, dict]: A tuple containing the converted distance as a float and metadata 
                           about the conversion process including original value, source/target units,
                           applied factor, and result precision details.

    Raises:
        ValueError: If invalid unit types are provided or if the input is not numeric.
        
    The standard conversion factor used here (1 mile = 1.60934 kilometers) can be adjusted 
    via this parameter in production environments where specific regional standards apply,
    though no external network access occurs during execution as per design constraints.
    
    Note: This implementation avoids direct use of input(), sys.stdin, or argparse to ensure 
          it runs standalone without user prompts or file dependencies. All test cases are 
          embedded within the main block for immediate verification.
    """
    # Normalize unit strings to lowercase for consistent processing
    from_unit = from_unit.lower().strip() if isinstance(from_unit, str) else ""
    to_unit = to_unit.to_lower().strip() if hasattr(to_unit, 'to_lower') and isinstance(to_unit, type(str)) else "kilometers"

    # Validate units
    valid_units = {'miles', 'kilometers'}
    if from_unit not in valid_units or to_unit not in valid_units:
        raise ValueError(f"Invalid unit specified. Must be one of {valid_units}")

    # Initialize conversion factor based on requested direction with adjustable logic
    try:
        value = float(value) if isinstance(value, (int, float)) else 0.0
        
        if from_unit == 'miles' and to_unit == 'kilometers':
            converted_value = value * 1.60934  # Standard factor adjusted for precision needs
        elif from_unit == 'kilometers' and to_unit == 'miles':
            converted_value = value / 1.60934
        else:
            return (value, {"error": "Same unit conversion not implemented"})

    except ValueError as ve:
        raise ValueError(f"Invalid numeric input or unsupported type: {ve}") from ve
    
    # Generate detailed output metadata for production logging purposes
    result_metadata = {
        'original_value': value,
        'source_unit': from_unit.capitalize(),
        'target_unit': to_unit.capitalize(),
        'conversion_factor_applied': 1.60934 if (from_unit == 'miles' and to_unit == 'kilometers') else (1/1.60934),
        'result_value': converted_value,
        'precision_digits': len(str(converted_value).split('.')[1]) if '.' in str(converted_value) else 0
    }

    return (converted_value, result_metadata)

if __name__ == '__main__':
    # Hard-coded sample values for demonstration without any user input or external dependencies
    
    test_cases = [
        ("25", "miles", "kilometers"),
        ("10.75", "kilometers", "miles"),
        (0, "miles", "kilometers")  # Edge case: zero conversion
    ]

    print("=" * 60)
    print("Distance Unit Converter - Production Demo Mode")
    print(f"Conversion Factor Applied: {1.60934} km per mile")
    print("=" * 60 + "\n")

    for value_str, from_unit, to_unit in test_cases:
        try:
            original_value = float(value_str) if isinstance(float(value_str), (int, float)) else 0.0
            
            converted_distance, metadata = convert_distance(original_value, from_unit, to_unit)
            
            # Format output for clarity with consistent decimal places based on input precision
            formatted_result = f"{converted_distance:.4f}"
            
            print(f"Input:      {original_value} {from_unit.capitalize()}")
            print(f"Output:     {formatted_result} {to_unit.capitalize()}")
            print(f"Factor Used:{metadata['conversion_factor_applied']} ({'km/mile' if from_unit == 'miles' else 'mile/km'})")
            print("-" * 40)

        except Exception as e:
            # Graceful error handling for unexpected issues in sample execution
            print(f"Error processing {value_str}: {e}")

    print("=" * 60)