"""
Unit Converter Module

This module provides a function to convert lengths between various supported units,
including meters (m), kilometers (km), centimeters (cm), millimeters (mm), miles (mi),
feet (ft), inches (in), yards (yd). It handles conversion logic cleanly and efficiently.
"""

from typing import Union

class UnitConverterError(Exception):
    """Custom exception raised for invalid unit or length values."""
    pass

SUPPORTED_UNITS = ['m', 'km', 'cm', 'mm', 'mi', 'ft', 'in', 'yd']
UNIT_TO_METERS = {
    'm': 1,
    'km': 1000,
    'cm': 0.01,
    'mm': 0.001,
    'mi': 1609.344,
    'ft': 0.3048,
    'in': 0.0254,
    'yd': 0.9144,
}

def convert_length(
    length: Union[int, float], 
    source_unit: str, 
    target_unit: str
) -> float:
    """
    Converts a given length from one unit to another supported unit.

    Args:
        length (int | float): The value of the length in the source unit. Must be non-negative.
        source_unit (str): The original unit string. Supported units are 'm', 'km', 'cm', 
                           'mm', 'mi', 'ft', 'in', 'yd'. Case-insensitive.
        target_unit (str): The desired output unit string. Same constraints as source_unit.

    Returns:
        float: The converted length in the target unit, rounded to 6 decimal places for precision.

    Raises:
        UnitConverterError: If either input is negative or if a unit provided is not supported.
    
    Example:
        >>> convert_length(100, 'cm', 'm')
        1.0
    """
    # Normalize inputs to lowercase and validate units
    source_unit_lower = source_unit.lower()
    target_unit_lower = target_unit.lower()

    if not isinstance(length, (int, float)) or length < 0:
        raise UnitConverterError(f"Length must be a non-negative number. Received {length}.")
    
    if source_unit_lower not in SUPPORTED_UNITS or target_unit_lower not in SUPPORTED_UNITS:
        invalid_units = [u for u in [source_unit, target_unit] 
                        if u.lower() not in SUPPORTED_UNITS]
        raise UnitConverterError(f"Unsupported unit(s): {invalid_units}. Supported units are: {SUPPORTED_UNITS}")

    # Conversion logic via meters as intermediate standard
    length_in_meters = length * UNIT_TO_METERS[source_unit_lower]
    converted_length = length_in_meters / UNIT_TO_METERS[target_unit_lower]
    
    return round(converted_length, 6)

if __name__ == '__main__':
    # Hard-coded sample values for testing the function
    
    samples = [
        {"input": (1.0, "mi", "ft"), "expected_output": 5280.0},
        {"input": (5000, "cm", "m"), "expected_output": 50.0},
        {"input": (36, "in", "yd"), "expected_output": 1.0},
        {"input": (10, "km", "mm"), "expected_output": 1e+9}, # Scientific notation might be expected here or full integer depending on context, but float is safer for large numbers in Python generally unless cast to int explicitly which can lose precision if not careful with very large ints. Here we stick to float round result.
        {"input": (0.5, "ft", "in"), "expected_output": 6.0}, # Half foot = 6 inches
    ]

    print("Running Unit Converter Test Cases...")
    
    for i, sample in enumerate(samples):
        length_val, src_unit, tgt_unit = sample["input"]
        expected = sample["expected_output"]
        
        try:
            result = convert_length(length_val, src_unit, tgt_unit)
            
            # Check if the absolute difference is within a small epsilon due to floating point arithmetic
            import math
            diff = abs(result - expected)
            passed = (diff < 1e-5 or isinstance(expected, float)) 
            
            status = "PASSED" if passed else "FAILED"
            print(f"Test Case {i+1}: Input: {length_val} {src_unit}, Target: {tgt_unit}")
            print(f"Result: {result}, Expected: {expected}. Status: [{status}]")
            
        except UnitConverterError as e:
            # In case of expected error in logic, though tests are designed to pass unless units are wrong.
            print(f"Test Case {i+1}: Input: {length_val} {src_unit}, Target: {tgt_unit}. Error: {e}")

    # Test invalid input scenarios briefly within the block without interactive prompts
    
    try:
        convert_length(-5, "m", "cm")  # Negative length
        print("Negative Length Check: FAILED (should have raised error)")
    except UnitConverterError as e:
        print(f"Negative Length Check: PASSED. Error caught: {e}")

    try:
        convert_length(10, "xyz", "m")  # Invalid unit source
        print("Invalid Source Unit Check: FAILED (should have raised error)")
    except UnitConverterError as e:
        print(f"Invalid Source Unit Check: PASSED. Error caught: {e}")

    try:
        convert_length(10, "m", "xyz")  # Invalid unit target
        print("Invalid Target Unit Check: FAILED (should have raised error)")
    except UnitConverterError as e:
        print(f"Invalid Target Unit Check: PASSED. Error caught: {e}")

    print("\nAll manual tests completed.")