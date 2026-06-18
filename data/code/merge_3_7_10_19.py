import math

def convert_time(duration: float, from_unit: str) -> dict[str, float]:
    """
    Converts a given time duration from one unit to all other standard units.
    
    Args:
        duration (float): The time value in the specified 'from_unit'.
        from_unit (str): The source unit ('seconds', 'minutes', 'hours', or 'days').
        
    Returns:
        dict[str, float]: A dictionary containing the converted values for all units.
                          Keys are lowercase strings representing the target units.
                          
    Raises:
        ValueError: If 'from_unit' is not one of the supported units.
    
    Note:
        This function assumes positive durations. Negative or zero inputs will 
        result in non-positive outputs but no exception is raised unless input validation 
        logic is explicitly added for negative numbers (not required by prompt, 
        so treated as valid mathematical operations).
        
        Supported conversions are based on standard time relationships:
        1 day = 24 hours
        1 hour = 60 minutes
        1 minute = 60 seconds
        
    Example:
        >>> convert_time(3600, 'seconds')
        {'seconds': 3600.0, 'minutes': 60.0, 'hours': 1.0, 'days': 0.04166...}
    """
    
    # Define conversion factors to base unit (seconds) for each input unit
    units_to_seconds = {
        'seconds': 1,
        'minutes': 60,
        'hours': 3600,
        'days': 86400
    }
    
    # Validate the source unit
    if from_unit not in units_to_seconds:
        raise ValueError(f"Unsupported time unit '{from_unit}'. Supported units are: seconds, minutes, hours, days.")

    # Convert input duration to total seconds first (base unit)
    base_value = duration * units_to_seconds[from_unit]
    
    # Calculate values for all other units using the base value in seconds
    result = {
        'seconds': round(base_value / 1.0, 6),
        'minutes': round((base_value / 60) if from_unit != 'minutes' else duration * 60, 6), # Handle direct mapping carefully to avoid double conversion logic errors in thought process, actually simpler: just divide base by factor
    }

    # Recalculate cleanly for all units based on total seconds
    result = {
        'seconds': round(base_value / 1.0, 6),
        'minutes': round(base_value / 60.0, 6),
        'hours': round(base_value / 3600.0, 6),
        'days': round(base_value / 86400.0, 6)
    }

    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        {'duration': 3600, 'unit': 'seconds'},      # Should yield 1 hour in hours/minutes/days and same in seconds
        {'duration': 90, 'unit': 'minutes'},         # Should yield 1.5 hours etc.
        {'duration': 24, 'unit': 'hours'},           # Should yield 1 day approx
        {'duration': 365, 'unit': 'days'}            # Large value test for days conversion
    ]

    print("Time Unit Conversion Results")
    print("-" * 40)

    for case in test_cases:
        duration = case['duration']
        unit = case['unit']
        
        try:
            converted_values = convert_time(duration, unit)
            
            # Format output nicely
            lines = [f"Input: {duration} {unit.capitalize()}"]
            print("\n".join(lines))
            
            for target_unit in ['seconds', 'minutes', 'hours', 'days']:
                val = converted_values[target_unit]
                if abs(val) < 0.001 and unit != 'days': # Avoid printing tiny floats unless significant
                    display_val = f"{val:.6f}"
                else:
                    display_val = str(round(val, 4))
                
                lines.append(f"Converted to {target_unit.capitalize()}: {display_val}")
            
            print("-" * 40)

        except ValueError as e:
            print(f"Error processing input {duration} in unit '{unit}': {e}")