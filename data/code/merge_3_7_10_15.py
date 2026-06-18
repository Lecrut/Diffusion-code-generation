import sys

def convert_time_to_units(duration: float, from_unit: str) -> dict[str, float]:
    """
    Converts a given time duration from one standard unit to all other units.
    
    Args:
        duration (float): The time value to convert.
        from_unit (str): The source unit ('seconds', 'minutes', 'hours', or 'days').
        
    Returns:
        dict[str, float]: A dictionary mapping each unit name to its corresponding converted value.
        
    Raises:
        ValueError: If the input duration is negative or if an invalid unit string is provided.
    
    Note:
        This function assumes standard SI definitions where 1 minute = 60 seconds, 
        1 hour = 60 minutes (3600 seconds), and 1 day = 24 hours (86400 seconds).
    """
    # Define conversion factors to base unit (seconds) for each input unit
    units_to_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }

    # Validate the from_unit argument against allowed values and ensure duration is non-negative
    valid_units = set(units_to_seconds.keys())
    
    if not isinstance(duration, (int, float)):
        raise TypeError(f"Duration must be a number, got {type(duration).__name__}")
        
    if duration < 0:
        raise ValueError("Time duration cannot be negative.")

    # Normalize the input unit string to lowercase for case-insensitive comparison
    from_unit_lower = from_unit.lower()
    
    if from_unit_lower not in valid_units:
        possible_options = ', '.join(valid_units)
        raise ValueError(f"Invalid time unit '{from_unit}'. Valid units are {possible_options}.")

    # Convert the input duration to seconds first (base unit), then back to all other target units
    total_seconds = duration * units_to_seconds[from_unit_lower]
    
    result = {}
    for unit_name, conversion_factor in units_to_seconds.items():
        value_in_target_unit = total_seconds / conversion_factor
        # Round to a reasonable precision (6 decimal places) only if the number is very small 
        # or extremely large to avoid floating point noise printing issues, otherwise keep standard representation.
        # However, for robustness in general use cases involving time, we usually prefer exact float representation unless specified.
        result[unit_name] = round(value_in_target_unit, 6)

    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input or external dependencies
    
    test_cases = [
        {
            'input_duration': 30.5,
            'from_unit': 'seconds'
        },
        {
            'input_duration': 120,
            'from_unit': 'minutes'
        },
        {
            'input_duration': 48,
            'from_unit': 'hours'
        },
        {
            'input_duration': -5, 
            'from_unit': 'seconds', # Should trigger ValueError
            'should_fail': True
        }
    ]

    print("Time Conversion Results")
    print("-" * 30)

    for i, case in enumerate(test_cases):
        duration = case['input_duration']
        from_unit = case['from_unit']
        
        try:
            converted_data = convert_time_to_units(duration, from_unit)
            
            if 'should_fail' not in case or not case.get('should_fail'):
                print(f"\nTest Case {i + 1}:")
                print(f"Input: {duration} {from_unit}")
                for unit_name, value in converted_data.items():
                    formatted_value = f"{value:.6f}" if isinstance(value, float) else str(value)
                    print(f"   {unit_name.capitalize()}: {formatted_value}")
            elif case.get('should_fail'):
                # Even though we expect failure here for demonstration of error handling logic in a robust script
                try:
                    converted_data = convert_time_to_units(duration, from_unit)
                    print(f"\nTest Case {i + 1} (Expected Error):")
                    print(f"Input: {duration} {from_unit}")
                    print("   ERROR HANDLING FAILED: Expected ValueError but script continued.")
                except Exception as e:
                    print(f"\nTest Case {i + 1} (Error Handling Verified):")
                    print(f"Input: {duration} {from_unit}")
                    print(f"Caught expected error: {type(e).__name__}: {e}")

        except ValueError as ve:
            if 'should_fail' not in case or not case.get('should_fail'):
                # This branch is theoretically unreachable given the logic above but kept for script robustness
                print(f"\nUnexpected Error during conversion:")
                print(f"Input: {duration} {from_unit}")
                print(f"Error Message: {ve}")
            else:
                pass # Expected error, ignore or log as needed
        
        except Exception as e:
            # Catch any unexpected runtime errors for logging purposes in the main block
            print(f"\nUnexpected exception occurred:")
            print(f"Input: {duration} {from_unit}")
            print(f"Error Type: {type(e).__name__}, Message: {e}")

    print("-" * 30)
    print("Conversion process completed.")