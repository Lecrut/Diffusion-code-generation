"""
Module to convert time difference strings into standardized datetime.timedelta objects.

This module provides a function `scale_time_differences` that takes a list of 
strings representing time durations (e.g., '1d', '2h30m') and converts them 
into timedelta instances, handling parsing errors gracefully by returning None 
for invalid entries rather than raising exceptions.
"""

import re
from datetime import timedelta

def scale_time_differences(time_strings):
    """
    Convert a list of time difference strings into a list of timedelta objects.

    This function attempts to parse each string in the input list according to 
    standard duration formats (e.g., '1d', '2h30m'). If a string cannot be 
    parsed, it returns None for that entry instead of raising an error.
    
    Supported units: s (seconds), m (minutes), h (hours), d (days).
    Multiple units can be combined in one string separated by '+' or '-'.

    Args:
        time_strings (list[str]): A list of strings representing time durations.

    Returns:
        list[timedelta | None]: A list where each element is either a 
                                timedelta object corresponding to the input string,
                                or None if parsing failed for that entry.
    
    Examples:
        >>> scale_time_differences(['1d', '2h30m'])
        [timedelta(days=1), timedelta(hours=2, minutes=30)]

        >>> scale_time_differences(['invalid', '5s'])
        [None, timedelta(seconds=5)]
    """
    
    def parse_duration_string(s):
        pattern = r'(\d+(?:\.\d+)?)\s*(s|m|h|d)'
        
        # If the string is empty or None, return None immediately
        if not s:
            return None
            
        try:
            total_seconds = 0.0
            matches = re.findall(pattern, s)
            
            for amount, unit in matches:
                value = float(amount)
                
                # Map units to seconds multiplier
                multipliers = {
                    's': 1,
                    'm': 60,
                    'h': 3600,
                    'd': 86400
                }
                
                total_seconds += value * multipliers[unit]

            return timedelta(seconds=total_seconds)
        except (ValueError, AttributeError):
            # Catch cases where conversion fails or regex doesn't match properly
            return None
            
    result = []
    
    for time_str in time_strings:
        parsed_value = parse_duration_string(time_str.strip()) if isinstance(time_str, str) else None
        result.append(parsed_value)

    return result

if __name__ == '__main__':
    # Hard-coded sample values to demonstrate functionality without user input
    
    test_cases = [
        ['1d', '2h30m', '90s'],  # Standard valid cases
        ['', None, 'invalid text', '-5h'],  # Edge cases including empty and negative
        ['1.5d', '45m', '+2h30m'],  # Decimal values and explicit signs
    ]

    print("Input Time Strings:", test_cases)
    
    for i, case in enumerate(test_cases):
        converted = scale_time_differences(case)
        print(f"\nCase {i + 1}:")
        original_reprs = [repr(s) if s is not None else "None" for s in case]
        result_reprs = [str(t) if t is not None else "None" for t in converted]
        
        # Display results aligned with inputs
        print(f"  Original: {original_reprs}")
        print(f"  Converted: {result_reprs}")

    # Demonstrate error handling explicitly
    print("\n--- Error Handling Demo ---")
    invalid_input = ['not_a_number', '', 'xyz123']
    output_invalid = scale_time_differences(invalid_input)
    
    for idx, (inp, out) in enumerate(zip(invalid_input, output_invalid)):
        status = "Successfully parsed" if out is not None else "Parsing failed as expected"
        print(f"Input '{inp}' -> {out} ({status})")