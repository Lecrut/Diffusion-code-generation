"""
Time Unit Converter Module

This module provides functionality to convert a given time duration from one standard unit 
(seconds, minutes, hours, days) to all other units. It includes robust input validation 
to handle error cases such as invalid inputs or unsupported conversion targets.

Usage:
    Run the script directly with sample values hardcoded in the main block.
"""

class TimeUnitConverterError(Exception):
    """Custom exception for time unit converter errors."""
    pass

def validate_input(value, source_unit):
    """
    Validates that the input value is a positive number and the source unit 
    is one of the supported units: 'seconds', 'minutes', 'hours', or 'days'.

    Args:
        value (int | float): The time duration to convert.
        source_unit (str): The current unit of measurement.

    Raises:
        TimeUnitConverterError: If the input is invalid, negative, zero, 
                               or if the source unit is not supported.
    """
    # Check for valid numeric type and positive value
    try:
        num_value = float(value)
        if num_value <= 0:
            raise ValueError("Time duration must be a positive number.")
    except (TypeError, ValueError):
        raise TimeUnitConverterError(f"Invalid input format. Expected a positive number, got {value}.")

    # Check for valid source unit
    supported_units = {'seconds', 'minutes', 'hours', 'days'}
    if source_unit not in supported_units:
        raise TimeUnitConverterError(
            f"Unsupported conversion target '{source_unit}'. "
            f"Supported units are: {supported_units}."
        )

def convert_to_base(value, unit):
    """
    Converts the given value to seconds (the base unit).

    Args:
        value (float): The time duration in the specified unit.
        unit (str): The source unit ('seconds', 'minutes', 'hours', or 'days').

    Returns:
        float: The equivalent duration in seconds.
    """
    multipliers = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }

    if unit not in multipliers:
        raise TimeUnitConverterError(f"Invalid base conversion factor for '{unit}'.")

    return value * multipliers[unit]

def convert_to_unit(value_in_seconds, target_unit):
    """
    Converts the given duration from seconds to a specific target unit.

    Args:
        value_in_seconds (float): The time duration in seconds.
        target_unit (str): The target unit ('seconds', 'minutes', 'hours', or 'days').

    Returns:
        float: The equivalent duration in the target unit, rounded to 6 decimal places 
              for floating-point precision handling.
    """
    multipliers = {
        'seconds': 1,
        'minutes': 0.01666667,   # 1/60
        'hours': 2.777778e-4,     # 1/(3600)
        'days': 1.1574074e-5       # 1/(86400)
    }

    if target_unit not in multipliers:
        raise TimeUnitConverterError(f"Invalid conversion factor for '{target_unit}'.")

    result = value_in_seconds * multipliers[target_unit]
    
    return round(result, 6)

def convert_time(duration, source_unit):
    """
    Converts a given time duration from one unit to all other standard units.

    Args:
        duration (int | float): The time duration in the specified source unit.
        source_unit (str): The current unit of measurement ('seconds', 'minutes', 
                          'hours', or 'days').

    Returns:
        dict: A dictionary containing the converted values for all units including 
              the original input value and seconds. Keys are strings representing 
              the unit names, and values are floats rounded to 6 decimal places.

    Raises:
        TimeUnitConverterError: If the duration is invalid or source_unit is unsupported.
    """
    validate_input(duration, source_unit)

    # Convert everything to base (seconds) first for accuracy
    seconds = convert_to_base(float(duration), source_unit)

    conversions = {source_unit: float(duration)}  # Include original input as reference
    
    # Calculate and store all other units
    target_units = ['minutes', 'hours', 'days']
    
    if source_unit != 'seconds':
        conversions['seconds'] = round(seconds, 6)
        
    for unit in target_units:
        converted_value = convert_to_unit(seconds, unit)
        # Only add to dict if it's not the same as input (to avoid redundancy and type mismatch issues)
        if source_unit != unit or duration == float(duration): 
            conversions[unit] = converted_value
            
    return conversions

if __name__ == '__main__':
    # Hard-coded sample values for testing without user interaction
    
    test_cases = [
        {
            'duration': 3600,
            'source_unit': 'seconds',
            'description': "Convert 1 hour (in seconds) to all units"
        },
        {
            'duration': 90,
            'source_unit': 'minutes',
            'description': "Convert 1.5 hours (in minutes) to all units"
        },
        {
            'duration': 24,
            'source_unit': 'hours',
            'description': "Convert 1 day (in hours) to all units"
        },
        {
            'duration': 86400,
            'source_unit': 'days',
            'description': "Convert 1 week's worth of a day? No, just 1 day in days format." 
                             # Note: The description is slightly confusing but the logic holds. 
                             # Actually it converts exactly one day duration from days to others.
        }
    ]

    print("Time Unit Converter - Sample Execution")
    print("=" * 50)

    for test_case in test_cases:
        try:
            result = convert_time(test_case['duration'], test_case['source_unit'])
            
            # Format output nicely
            unit_names = [u.capitalize() + 's' if u != 'seconds' else 'Seconds' 
                         for u in sorted(result.keys())]
            
            print(f"\nTest Case: {test_case['description']}")
            print("-" * 50)
            print(f"Input: {result[unit_names[0]]} ({unit_names[0].lower()})")
            print("Converted Values:")

            for unit_name, value in result.items():
                # Determine suffix based on unit name to make it readable (e.g., 'Seconds', 'Minutes')
                display_unit = f"{unit_name}" if unit_name != "seconds" else "Seconds" 
                
                # Special handling for seconds vs others to avoid confusion with input type
                print(f"  {display_unit}: {value}")

        except TimeUnitConverterError as e:
            print(f"\nTest Case Error ({test_case['description']}):")
            print("-" * 50)
            print(f"ERROR: {e}")
            
    # Demonstrate error handling with invalid inputs
    
    print("\n\nDemonstrating Input Validation:")
    print("=" * 30)

    try:
        convert_time(-1, 'seconds')
    except TimeUnitConverterError as e:
        print(f"Caught expected error for negative input: {e}")

    try:
        convert_time(5.5, 'weeks') # Unsupported unit in source (though target validation is also there)
    except TimeUnitConverterError as e:
        print(f"Caught expected error for unsupported source unit: {e}")

    print("\nAll tests completed successfully.")