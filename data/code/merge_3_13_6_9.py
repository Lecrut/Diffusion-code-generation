import re
from datetime import timedelta

def parse_timezone_config(content: str) -> dict[str, int]:
    """
    Parses a configuration string containing timezone definitions in the format 'name = offset_hours'.
    
    Args:
        content (str): The raw configuration text.
        
    Returns:
        dict: A dictionary mapping zone names to their hour offsets relative to UTC.
    """
    zones = {}
    # Pattern matches lines like "zone_name = 5" or "zone_name = -3"
    pattern = r'^\s*(\w+)\s*=\s*(-?\d+\.?)(?:\s*$|\s+#.*)$'
    
    for line in content.strip().split('\n'):
        match = re.match(pattern, line)
        if not match:
            continue
            
        zone_name = match.group(1).strip()
        offset_str = match.group(2).replace(',', '.')  # Handle potential comma decimals
        
        try:
            offset_hours = float(offset_str)
            zones[zone_name] = int(round(offset_hours))
        except ValueError:
            continue
            
    return zones

def calculate_timezone_difference(zone_a: str, zone_b: str, config_zones: dict[str, int]) -> timedelta:
    """
    Calculates the time difference between two timezone definitions.
    
    Args:
        zone_a (str): Name of the first timezone.
        zone_b (str): Name of the second timezone.
        config_zones (dict): Dictionary containing all parsed timezone offsets.
        
    Returns:
        timedelta: The duration representing the time difference between zones A and B.
                   Positive means Zone A is ahead of Zone B.
    """
    if zone_a not in config_zones or zone_b not in config_zones:
        raise ValueError(f"Unknown timezone(s): {zone_a}, {zone_b}")
    
    offset_a = config_zones[zone_a]
    offset_b = config_zones[zone_b]
    
    difference_hours = offset_a - offset_b
    
    return timedelta(hours=difference_hours)

if __name__ == '__main__':
    # Hard-coded sample configuration content simulating a file read
    config_content = """
utc_standard = 0
eastern_time_zone = -4.5
central_time_zone = -6.0
"""

    parsed_zones = parse_timezone_config(config_content)
    
    zone_a_name = "eastern_time_zone"
    zone_b_name = "central_time_zone"
    
    try:
        diff = calculate_timezone_difference(zone_a_name, zone_b_name, parsed_zones)
        
        print(f"Difference between {zone_a_name} and {zone_b_name}:")
        if diff.total_seconds() > 0:
            print(f"{diff.total_seconds()} hours ({abs(diff)} ahead)")
        else:
            print(f"-{abs(diff.total_seconds())} hours ({abs(diff)} behind)")
            
    except ValueError as e:
        print(f"Error processing timezones: {e}")