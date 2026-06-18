import datetime

def scale_time_differences(time_strings: list) -> list:
    """
    Converts a list of time difference strings into standardized datetime.timedelta objects.
    
    Args:
        time_strings (list): A list of strings representing time differences. 
                             Expected formats include "1 day", "2 hours 30 minutes", etc.,
                             or simple numeric values with units like '5d', 'h3m'.
                             
    Returns:
        list: A list of datetime.timedelta objects corresponding to the input strings.
        
    Raises:
        ValueError: If a string cannot be parsed into a valid time difference.
    
    Note:
        This function attempts robust parsing for common textual representations 
        of durations (e.g., "1 day", "2h30m"). Errors are raised immediately upon failure,
        rather than being silently ignored or returning None, to ensure the caller can handle invalid inputs explicitly if needed.
    
    """
    results = []

    # Regex patterns for parsing various time string formats:
    # 1. Full words: "X days", "Y hours Z minutes" -> \d+(?:\s+days?)?(?:\s+hours?\s+\d*(?:\s+minutes?))?
    # 2. Abbreviated/compact: "5d", "h3m", "10h30m" -> (\d+)([dhH][dmM]|\d+[dhD])
    
    patterns = [
        (r'^(\d+)\s*days?$', 'day'),      # e.g., "2 days", "5d"
        (r'^(\d+)\s*(?:hours?)?(?:\s+\d+(?: minutes?))?$', 'hour'),               # e.g., "1 hour 30 min"
    ]

    for i, time_str in enumerate(time_strings):
        try:
            if not isinstance(time_str, str):
                raise ValueError(f"Element at index {i} is not a string.")

            parsed_td = None
            
            # Attempt pattern matching with full words first (more readable)
            import re
            for regex_pattern in patterns:
                match = re.match(regex_pattern[0], time_str.strip())
                if match:
                    groups = match.groups()
                    
                    total_seconds = 0
                    
                    # Handle 'days' component
                    day_part = None
                    hour_part = None
                    minute_part = None
                    
                    for idx, group in enumerate(groups):
                        val = int(group)
                        
                        unit_name = regex_pattern[1] if len(regex_pattern) > 1 else "day"
                        
                        # Special handling for patterns with multiple units like "X hours Y minutes"
                        # We need to identify which part is day, hour, or minute.
                        # Since our simple regexes above are limited in capturing mixed complex cases 
                        # without specific grouping logic, let's implement a more flexible parser below.

                    break  # Found a match for this format
            
            # --- Fallback Flexible Parser Logic (more robust than the initial quick patterns) ---
            
            if parsed_td is None:
                clean_str = time_str.strip().lower()
                
                total_seconds = 0
                
                # Extract numeric values and units dynamically
                numbers = re.findall(r'\d+', clean_str)
                unit_chars = [c for c in set(clean_str.lower()) if c.isdigit() or not any(c == n[1] for n in zip(range(len(numbers)), range(1, len(numbers)+len(unit_chars)))) is False and (clean_str.replace('.', '').replace('-', '')).count(c) > 0]
                
                # Simpler extraction: find all numbers and their associated units
                tokens = re.findall(r'(\d+)([dhDmH])', clean_str)
                
                if not tokens:
                    raise ValueError(f"Could not parse time string: '{time_str}'")

                for num, unit in tokens:
                    val = int(num)
                    
                    # Determine multiplier based on unit (case insensitive check handled by lower())
                    if 'd' or 'D' == unit[0]:
                        total_seconds += val * 24 * 60 * 60
                    elif 'h' in unit:
                        total_seconds += val * 60 * 60
                    else: # m, M (minutes)
                        total_seconds += val * 60
                
                parsed_td = datetime.timedelta(seconds=total_seconds)

            results.append(parsed_td)
            
        except Exception as e:
            raise ValueError(f"Failed to parse time string '{time_str}': {str(e)}") from None

if __name__ == '__main__':
    # Hard-coded sample values for testing without user input or external dependencies.
    samples = [
        "1 day",
        "2 hours 30 minutes",
        "5d",
        "h3m",
        "10h30m", 
        "3 days, 4 hours", # Complex case if regex handles it (currently simplified)
    ]

    try:
        converted = scale_time_differences(samples)
        
        print("Converted time differences:")
        for i, td in enumerate(converted):
            print(f"Original {samples[i]} -> {td} seconds ({td.total_seconds()}s)")
            
        # Test error handling with an invalid string
        print("\nTesting error handling...")
        try:
            scale_time_differences(["invalid input"])
        except ValueError as ve:
            print(f"Catch expected error for 'invalid input': {ve}")

    except Exception as e:
        print(f"Unexpected error in main block: {e}")