def convert_time(time_value: float, source_unit: str, target_unit: str) -> float:
    """
    Converts a time value from one unit (seconds, minutes, hours) to another.
    
    Args:
        time_value (float): The numerical value of the time.
        source_unit (str): The original unit ('s', 'm', or 'h').
        target_unit (str): The desired unit ('s', 'm', or 'h').
        
    Returns:
        float: The converted time value in the target unit.
        
    Raises:
        ValueError: If invalid units are provided.
    """
    
    # Define conversion factors to seconds as a common base
    to_seconds = {
        's': 1,
        'm': 60,
        'h': 3600
    }
    
    from_seconds = {
        's': 1,
        'm': 60.0 / 60, # Convert minutes to seconds for calculation logic if needed, 
                         # but simpler is: value_in_source * factor_to_base -> base_value
        'h': 3600.0 / 60
    }

    # Normalize input units and validate
    source_unit = source_unit.lower()
    target_unit = target_unit.lower()
    
    if source_unit not in to_seconds or target_unit not in to_seconds:
        raise ValueError(f"Invalid unit provided. Must be one of 's', 'm', 'h'.")

    # Convert the input value to seconds first (standardizing on a base)
    time_in_seconds = time_value * to_seconds[source_unit]
    
    # Then convert from seconds to the target unit
    converted_time = time_in_seconds / to_seconds[target_unit]
    
    return converted_time

if __name__ == '__main__':
    # Sample test cases running without user input or external dependencies
    
    # Test 1: Convert 3 hours to minutes
    result_1 = convert_time(3, 'h', 'm')
    print(f"3 hours is {result_1} minutes")

    # Test 2: Convert 90 seconds to minutes
    result_2 = convert_time(90, 's', 'm')
    print(f"90 seconds is {result_2} minutes")

    # Test 3: Convert 0.5 hours to seconds
    result_3 = convert_time(0.5, 'h', 's')
    print(f"0.5 hours is {result_3} seconds")

    # Test 4: Direct conversion from minutes to seconds (e.g., 12 min -> s)
    result_4 = convert_time(12, 'm', 's')
    print(f"12 minutes is {result_4} seconds")

    # Test 5: Edge case - zero value
    result_5 = convert_time(0, 'h', 's')
    print(f"0 hours is {result_5} seconds")