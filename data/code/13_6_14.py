import re

def parse_timezone_config(config_content: str) -> dict[str, int]:
    """
    Parses a configuration string containing timezone definitions in the format 'TZ=HOURS'.
    
    Returns a dictionary mapping timezone identifiers to their hour offsets.
    Only entries matching the pattern TZ=<integer> are considered for time scale calculation.
    The parsing logic focuses purely on extracting integer hours from the text, ignoring 
    DST adjustments or other complex rules as per the task requirement of focusing on 
    the time scale relationship.
    
    Args:
        config_content (str): String containing timezone definitions. Expected format 'TZ=<hours>'.
        
    Returns:
        dict[str, int]: Dictionary with timezone keys and integer hour values.
    """
    pattern = r'TZ=([+-]?\d+)'
    matches = re.findall(pattern, config_content)
    
    result = {}
    for match in matches:
        try:
            hours = int(match)
            # Store the first two valid entries found to simulate reading "two" definitions.
            if len(result) < 2:
                tz_name = f"TZ_{len(result)+1}"
                result[tz_name] = hours
        except ValueError:
            continue
    
    return result

def calculate_hour_difference(tz_a: int, tz_b: int) -> float:
    """
    Calculates the difference in hours between two timezone offsets.
    
    Args:
        tz_a (int): Hour offset for the first timezone.
        tz_b (int): Hour offset for the second timezone.
        
    Returns:
        float: The absolute difference in hours.
    """
    return abs(tz_a - tz_b)

if __name__ == '__main__':
    # Hard-coded sample configuration string simulating a config file content.
    # No user input, stdin, or network access is used.
    config_content = '''UTC=0
EASTERN=-5
WESTERN=+4'''

    timezones = parse_timezone_config(config_content)

    if len(timezones) >= 2:
        tz1_name, hours1 = list(timezones.items())[0]
        tz2_name, hours2 = list(timezones.items())[1]
        
        difference_hours = calculate_hour_difference(hours1, hours2)
        print(f"Time scale relationship between {tz1_name} and {tz2_name}:")
        print(f"Difference in hours: {difference_hours}")
    else:
        print("Insufficient timezone definitions provided.")